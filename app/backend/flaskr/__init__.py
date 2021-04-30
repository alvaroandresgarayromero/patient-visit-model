from flask import Flask, jsonify
from .models import *
from .auth import *


POSTGRES_PORT = os.environ.get('POSTGRES_USER', 'none')


def create_app():
    app = Flask(__name__)
    #setup_db(app)

    @app.route('/', methods=['POST', 'GET'])
    def health():
        return jsonify({'success': POSTGRES_PORT})

    return app


if __name__ == '__main__':
    APP = create_app()
    APP.run(host='0.0.0.0')
