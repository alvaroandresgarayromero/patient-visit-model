import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json


POSTGRES_DB = os.environ.get('POSTGRES_DB', None)
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', None)
POSTGRES_USER = os.environ.get('POSTGRES_USER', None)
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', None)



database_path = "postgresql://{}:{}@localhost:{}/{}".format(POSTGRES_USER,
                                                            POSTGRES_PASSWORD,
                                                            POSTGRES_PORT,
                                                            POSTGRES_DB)


db = SQLAlchemy()


# psql -h localhost -p 5432 -d patientnursedb -U postgres --password

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, db_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    print(POSTGRES_PASSWORD)
    # print('model db print')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
