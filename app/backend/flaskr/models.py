from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from . import config
from .logprint import _logger

LOG = _logger()

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""


def setup_db(app):
    LOG.debug("database url: %s", config.DATABASE_URL)

    app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.drop_all()
    db.create_all()


class Visit(db.Model):
    __tablename__ = 'Visit'

    id = Column(db.Integer, primary_key=True)
    nurse_auth0_id = Column(db.String, nullable=False)
    patient_auth0_id = Column(db.String, nullable=False)
    visit_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, nurse_auth0_id, patient_auth0_id, visit_time):
        self.nurse_auth0_id = nurse_auth0_id
        self.patient_auth0_id = patient_auth0_id
        self.visit_time = visit_time

    def format(self):
        return {
            'id': self.id,
            'nurse_auth0_id': self.nurse_auth0_id,
            'nurse_name': 'na',
            'patient_auth0_id': self.patient_auth0_id,
            'patient_name': 'na',
            'visit_time': self.visit_time
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
