from sqlalchemy import Column, exc
from flask_sqlalchemy import SQLAlchemy
from ..logprint import _logger


LOG = _logger(__name__)

db = SQLAlchemy()


class Visit(db.Model):
    __tablename__ = 'Visit'

    id = Column(db.Integer, primary_key=True)
    nurse_id = Column(db.String, nullable=False)
    patient_id = Column(db.String, nullable=False)
    visit_time = db.Column(db.DateTime, nullable=False)

    vitalsigns = db.relationship('VitalSign', backref='visit', lazy='select')

    def __init__(self, nurse_id, patient_id, visit_time):
        self.nurse_id = nurse_id
        self.patient_id = patient_id
        self.visit_time = visit_time

    def long_format(self, nurse_name, patient_name):
        return {
            'id': self.id,
            'nurse_id': self.nurse_id,
            'nurse_name': nurse_name,
            'patient_id': self.patient_id,
            'patient_name': patient_name,
            'visit_time': self.visit_time.strftime("%m/%d/%Y, %H:%M:%S")
        }

    def short_format(self):
        return {
            'id': self.id,
            'nurse_id': self.nurse_id,
            'patient_id': self.patient_id,
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

    def reset(self):
        db.session.rollback()

class VitalSign(db.Model):
    __tablename__ = 'VitalSign'

    # A visit_id cannot have more than one vital sign record
    __table_args__ = (db.UniqueConstraint('visit_id'),)

    id = Column(db.Integer, primary_key=True)
    visit_id = db.Column(db.Integer, db.ForeignKey('Visit.id'), nullable=False)
    tempCelsius = Column(db.Integer, nullable=False)

    def __init__(self, visit_id, tempCelsius):
        self.visit_id = visit_id
        self.tempCelsius = tempCelsius

    def short_format(self):
        return {
            'id': self.id,
            'visit_id': self.visit_id,
            'tempCelsius': self.tempCelsius,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def reset(self):
        db.session.rollback()
