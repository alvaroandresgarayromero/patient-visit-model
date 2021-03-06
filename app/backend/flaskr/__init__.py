import os
from flask import Flask, current_app
from .db.models import *
from .logprint import _logger
from .api.routes import api
from .db import config
from . import commands

LOG = _logger('flaskr.__init__')

FLASK_ENVIRONMENT = os.environ.get('FLASK_ENV', None)


def create_app(a_configclass=config.configs[FLASK_ENVIRONMENT]):
    app = Flask(__name__)

    app.config.from_object(a_configclass())

    db.init_app(app)
    commands.init_app(app)

    # create routes
    app.register_blueprint(api)

    return app
