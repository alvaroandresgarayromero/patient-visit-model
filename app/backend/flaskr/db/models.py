from sqlalchemy import Column
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
