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


class Nurse(db.Model):
    __tablename__ = 'Nurse'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String,  nullable=False)
    visits = db.relationship('Visit', backref='nurses', lazy='joined')

    def __init__(self, name):
        self.name = name

    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }

    '''
     insert()
         inserts a new model into a database
         the model must have a unique name
         the model must have a unique id or null id
         EXAMPLE
             nurse = Nurse(name=a_name)
             nurse.insert()
     '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            nurse = Nurse(name=a_name)
            nurse.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            nurse = Nurse.query.filter(Nurse.id == id).one_or_none()
            nurse.name = 'Courtney'
            nurse.update()
    '''

    def update(self):
        db.session.commit()


class Patient(db.Model):
    __tablename__ = 'Patient'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String, nullable=False)
    gender = Column(db.String,  nullable=False)
    age = Column(db.Integer,  nullable=False)
    visits = db.relationship('Visit', backref='patients', lazy='joined')

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Visit(db.Model):
    __tablename__ = 'Visit'

    id = Column(db.Integer, primary_key=True)
    nurse_id = db.Column(db.Integer, db.ForeignKey('Nurse.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('Patient.id'), nullable=False)
    visit_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, nurse_id, patient_id, visit_time):
        self.nurse_id = nurse_id
        self.patient_id = patient_id
        self.visit_time = visit_time

    def format(self):
        return {
            'id': self.id,
            'nurse_id': self.nurse_id,
            'nurse_name': self.Nurse.name,
            'patient_id': self.patient_id,
            'patient_name': self.Patient.name,
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
