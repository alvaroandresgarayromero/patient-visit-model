import os
from flask import Flask, jsonify, request, abort
from .models import *
from .auth import *


def create_app():
    app = Flask(__name__)
    setup_db(app)

    @app.route('/', methods=['GET'])
    def index():
        # quick verification response to verify
        # that the server is active
        return jsonify({'success': True})

    @app.route('/nurses/create', methods=['POST'])
    def create_nurse():
        body = request.get_json()

        try:
            nurse = Nurse(name=body.get('name'))
            nurse.insert()
        except:
            abort(422)

        return jsonify(nurse.format())

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
