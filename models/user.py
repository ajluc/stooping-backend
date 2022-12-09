from models.db import db
from datetime import datetime

class User(db.Model):
  # Define the table name
  __tablename__ = 'users'
  # Create the columns of the table
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))
  email = db.Column(db.String(255))
  password_digest = db.Column(db.String(255))
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())

  # Set up constructor for the model
  def __init__(self, name, email, password_digest):
    self.name = name
    self.email = email
    self.password_digest = password_digest