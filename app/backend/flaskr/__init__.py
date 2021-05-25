from flask import Flask, current_app
from .db.models import *
from .auth0 import auth
from .logprint import _logger
from .auth0.authManagementAPI import *
from .api.routes import api
from .db import config
from . import commands

LOG = _logger('flaskr.__init__')

FLASK_ENVIRONMENT = os.environ.get('FLASK_ENV', None)


def create_app(a_configclass=config.configs[FLASK_ENVIRONMENT]):
    app = Flask(__name__)

    app.config.from_object(a_configclass())

    print(app.app_context().app.config)

    db.init_app(app)
    commands.init_app(app)

    # create routes
    app.register_blueprint(api)

    return app

