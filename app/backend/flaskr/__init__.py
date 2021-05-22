from flask import Flask, jsonify, request, abort
from .db.models import *
from .auth0 import auth
from .logprint import _logger
from .auth0.authManagementAPI import *
from datetime import *

LOG = _logger('flaskr.__init__')


def create_app():

    app = Flask(__name__)
    setup_db(app)

    # build Auth0 Management API
    builder = Auth0ManagementAPIBuilder()
    auth0api = builder.load_base_url(). \
        load_access_token(). \
        load_users(). \
        load_roles(). \
        build()

    @app.route('/', methods=['GET'])
    @app.route('/login-results', methods=['GET'])
    def index():
        # quick verification response to verify
        # that the server is active
        return jsonify({'success': True})

    @app.route('/visits/create', methods=['POST'])
    @auth.requires_auth(permission='post:visits')
    def create_visit(payload):
        body = request.get_json()

        try:
            visit = Visit(nurse_id=payload.get('sub'),
                          patient_id=body.get('patient_id'),
                          visit_time=datetime.now())

            # fetching names also verifies whether the user id exist in auth0
            names = auth0api.get_user_name([visit.nurse_id, visit.patient_id])

            visit.insert()

            selection = Visit.query.get(visit.id)

            result = selection.format(names[0], names[1])

        except:
            abort(422)

        return jsonify({'success': True,
                        'data': result})

    @app.route('/visits/<int:a_id>', methods=['PATCH'])
    @auth.requires_auth(permission='update:visits')
    def update_visit(payload, a_id):
        body = request.get_json()

        try:
            update_patient = body.get('patient_id')

            visit = Visit.query.get(a_id)
            visit.patient_id = update_patient

            # fetching names also verifies whether the user id exist in auth0
            names = auth0api.get_user_name([visit.nurse_id, visit.patient_id])

            visit.update()

            selection = Visit.query.get(a_id)
            result = selection.format(names[0], names[1])

        except:
            abort(422)

        return jsonify({'success': True,
                        'data': result})


    '''
    @app.route('/nurses/<int:a_id>', methods=['GET'])
    def get_nurse(a_id):
        try:
            nurse = Nurse.query.get(a_id)
            output = nurse.format()

        except:
            abort(404)

        return jsonify(output)

    @app.route('/patients/<int:a_id>', methods=['GET'])
    def get_patient(a_id):
        try:
            patient = Patient.query.get(a_id)
            output = patient.format()
        except:
            abort(404)

        return jsonify(output)

    @app.route('/nurses/<int:a_id>', methods=['PATCH'])
    def update_nurse(a_id):

        body = request.get_json()

        try:
            nurse = Nurse.query.get(a_id)

            nurse.name = body.get('name')

            nurse.update()

            output = nurse.format()

        except:
            abort(404)

        return jsonify(output)

    @app.route('/patients/<int:a_id>', methods=['PATCH'])
    def update_patient(a_id):

        body = request.get_json()

        try:
            patient = Patient.query.get(a_id)

            patient.name = body.get('name')
            patient.gender = body.get('gender')
            patient.age = body.get('age')

            patient.update()

            output = patient.format()
        except:
            abort(404)

        return jsonify(output) 
    '''

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
        }), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not Found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    @app.errorhandler(auth.AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app


if __name__ == '__main__':
    APP = create_app()
    APP.run(host='0.0.0.0')
