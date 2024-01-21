"""Models for pet adoption."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)


class Pet(db.Model):
  """Pets table"""

  __tablename__ = 'pets'

  id = db.Column(db.Integer, primary_key = True, autoincrement=True)
  name = db.Column(db.String, nullable=False)
  species = db.Column(db.String, nullable=False)
  img_url = db.Column(db.String, nullable=True)
  age = db.Column(db.Integer, nullable=True)
  notes = db.Column(db.String, nullable=True)
  status = db.Column(db.Boolean, default=True)