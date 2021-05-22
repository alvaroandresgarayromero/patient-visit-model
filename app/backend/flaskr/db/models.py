from sqlalchemy import Column
from flask_sqlalchemy import SQLAlchemy
from . import config
from ..logprint import _logger

LOG = _logger(__name__)

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""


def setup_db(app, database_url=config.DATABASE_URL):
    LOG.debug("database url: %s", database_url)

    app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.drop_all()
    db.create_all()


class Visit(db.Model):
    __tablename__ = 'Visit'

    id = Column(db.Integer, primary_key=True)
    nurse_id = Column(db.String, nullable=False)
    patient_id = Column(db.String, nullable=False)
    visit_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, nurse_id, patient_id, visit_time):
        self.nurse_id = nurse_id
        self.patient_id = patient_id
        self.visit_time = visit_time

    def format(self, nurse_name, patient_name):
        return {
            'id': self.id,
            'nurse_id': self.nurse_id,
            'nurse_name': nurse_name,
            'patient_id': self.patient_id,
            'patient_name': patient_name,
            'visit_time': self.visit_time.strftime("%m/%d/%Y, %H:%M:%S")
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
