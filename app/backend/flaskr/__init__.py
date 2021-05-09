import os
from flask import Flask, jsonify, request, abort
from .models import *
from .auth import *


def create_app():
    app = Flask(__name__)
    setup_db(app)

    @app.route('/verify_server_is_running', methods=['GET'])
    def index():
        # quick verification response to verify
        # that the server is active
        return jsonify({'success': True})

    @app.route('/visits/create', methods=['POST'])
    def create_visit():
        body = request.get_json()

        try:
            visit = Visit(nurse_auth0_id=body.get('nurse_auth0_id'),
                          patient_auth0_id=body.get('nurse_auth0_id'),
                          visit_time=body.get('visit_time'))
            visit.insert()
            output = visit.format()
        except:
            abort(422)

        return jsonify(output)

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

    return app


if __name__ == '__main__':
    APP = create_app()
    APP.run(host='0.0.0.0')
