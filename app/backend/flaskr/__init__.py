from flask import Flask, jsonify
from .models import *
from .auth import *


def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['POST', 'GET'])
    def health():
        return jsonify({'success': True})

    return app


if __name__ == '__main__':
    APP = create_app()
    APP.run(host='0.0.0.0')
