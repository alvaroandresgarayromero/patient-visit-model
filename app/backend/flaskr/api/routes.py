from flask import jsonify, request, abort, Blueprint
from ..auth0 import auth
from ..auth0.authManagementAPI import *
from datetime import *
from ..db.models import *

api = Blueprint('api', __name__)

# build Auth0 Management API
builder = Auth0ManagementAPIBuilder()
auth0api = builder.load_base_url(). \
    load_access_token(). \
    load_users(). \
    load_roles(). \
    build()


@api.route('/', methods=['GET'])
@api.route('/login-results', methods=['GET'])
def index():
    # quick verification response to verify
    # that the server is active
    return jsonify({'success': True})


@api.route('/visits/create', methods=['POST'])
@auth.requires_auth(permission='post:visits')
def create_visit(payload):
    body = request.get_json()

    try:
        visit = Visit(nurse_id=body.get('nurse_id'),
                      patient_id=body.get('patient_id'),
                      visit_time=datetime.now())

        # fetching names also verifies whether the user
        # id exist in auth0
        names = auth0api.get_user_name([visit.nurse_id,
                                        visit.patient_id])

        visit.insert()

        selection = Visit.query.get(visit.id)

        result = selection.long_format(names[0], names[1])

    except exc.SQLAlchemyError:
        visit.reset()
        abort(422)
    except:
        abort(422)

    return jsonify({'success': True,
                    'data': result})


@api.route('/visits/<int:a_id>', methods=['PATCH'])
@auth.requires_auth(permission='patch:visits')
def update_visit(payload, a_id):
    body = request.get_json()

    try:
        visit = Visit.query.get(a_id)
        assert visit is not None, f'visit record not found {a_id}'

        if 'patient_id' in body:
            visit.patient_id = body.get('patient_id')

        if 'nurse_id' in body:
            visit.nurse_id = body.get('nurse_id')

        # fetching names also verifies whether the user
        # id exist in auth0
        names = auth0api.get_user_name([visit.nurse_id,
                                        visit.patient_id])

        visit.update()

        selection = Visit.query.get(a_id)

        result = selection.long_format(names[0], names[1])

    except exc.SQLAlchemyError:
        visit.reset()
        abort(422)
    except:
        abort(422)

    return jsonify({'success': True,
                    'data': result})


@api.route('/visits/<int:a_id>', methods=['DELETE'])
@auth.requires_auth(permission='delete:visits')
def delete_visit(payload, a_id):

    try:
        visit = Visit.query.get(a_id)

        assert visit is not None, f'visit record not found {a_id}'

        visit.delete()

    except exc.SQLAlchemyError:
        visit.reset()
        abort(422)
    except:
        abort(422)

    return jsonify({'success': True,
                    'visit_id': a_id})


@api.route('/vital-signs/create', methods=['POST'])
@auth.requires_auth(permission='post:vital-signs')
def create_vitalsign(payload):
    body = request.get_json()

    try:
        vitalsign = VitalSign(visit_id=body.get('visit_id'),
                              tempCelsius=body.get('tempCelsius'))

        vitalsign.insert()

        selection = VitalSign.query.get(vitalsign.id)

        result = selection.short_format()

    except exc.SQLAlchemyError:
        vitalsign.reset()
        abort(422)
    except:
        abort(422)

    return jsonify({'success': True,
                    'data': result})


@api.route('/vital-signs/<int:a_id>', methods=['PATCH'])
@auth.requires_auth(permission='patch:vital-signs')
def update_vitalsign(payload, a_id):
    body = request.get_json()

    try:
        vitalsign = VitalSign.query.get(a_id)
        assert vitalsign is not None, f'vital sign record not found {a_id}'

        if 'visit_id' in body:
            vitalsign.visit_id = body.get('visit_id')

        if 'tempCelsius' in body:
            vitalsign.tempCelsius = body.get('tempCelsius')

        vitalsign.update()

        selection = VitalSign.query.get(a_id)
        result = selection.short_format()

    except exc.SQLAlchemyError:
        vitalsign.reset()
        abort(422)
    except:
        abort(422)


    return jsonify({'success': True,
                    'data': result})


@api.route('/vital-signs/<int:a_id>', methods=['DELETE'])
@auth.requires_auth(permission='delete:vital-signs')
def delete_vitalsigns(payload, a_id):

    try:
        vitalsign = VitalSign.query.get(a_id)

        assert vitalsign is not None, f'vital sign record not found {a_id}'

        vitalsign.delete()

    except exc.SQLAlchemyError:
        vitalsign.reset()
        abort(422)
    except:
        abort(422)

    return jsonify({'success': True,
                    'vitalsign_id': a_id})


@api.route('/patients/search', methods=['GET'])
@auth.requires_auth(permission='read:patient-data')
def search_patient(payload):
    body = request.get_json()

    try:
        patient_id = body.get('patient_id')

        visits = Visit.query.filter_by(patient_id=patient_id).all()
        assert visits != [], f'no patients found in visit record with id: {patient_id}'

        result = format_visit_and_vital_sign_data(visits)

    except exc.SQLAlchemyError:
        visits.reset()
        abort(404)
    except:
        abort(404)

    return jsonify({'success': True,
                    'data': result})


@api.route('/patients/search/user', methods=['GET'])
@auth.requires_auth(permission='read:restrictive-patient-data')
def get_user_patient_record(payload):

    try:
        # use decoded payload data to get patient id (active user)
        patient_id = payload.get('sub')

        visits = Visit.query.filter_by(patient_id=patient_id).all()
        assert visits != [], f'no patients found in visit record with id: {patient_id}'

        result = format_visit_and_vital_sign_data(visits)

    except exc.SQLAlchemyError:
        visits.reset()
        abort(404)
    except:
        abort(404)

    return jsonify({'success': True,
                    'data': result})


'''
Packages visits and vital sign data 

INPUT: visits [list] : list of visit objects from Visit class
OUTPUT: result [list] : Reformatted data 
'''
def format_visit_and_vital_sign_data(visits):
    result = []
    for visit in visits:
        names = auth0api.get_user_name([visit.nurse_id,
                                        visit.patient_id])

        visit_format = visit.long_format(names[0], names[1])

        if not visit.vitalsigns:
            # no vital signs have been documented in this visit
            vitalsign_format = []
        else:
            vitalsign_format = visit.vitalsigns[0].short_format()

        element = {"visit": visit_format,
                   "vitalSign": vitalsign_format}

        result.append(element)
    return result


@api.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
    }), 400


@api.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Unauthorized"
    }), 401


@api.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not Found"
    }), 404


@api.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable"
    }), 422


@api.errorhandler(auth.AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response
