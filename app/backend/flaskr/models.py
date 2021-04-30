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
    db.create_all()


class Category(db.Model):
  __tablename__ = 'category'

  id = Column(Integer, primary_key=True)
  type = Column(String)

  def __init__(self, type):
    self.type = type

  def format(self):
    return {
      'id': self.id,
      'type': self.type
    }