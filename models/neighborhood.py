from models.db import db
from datetime import datetime

class Neighborhood(db.Model):
  # Define the table name
  __tablename__ = 'neighborhoods'
  # Create the columns of the table
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
  comments = db.relationship("Comment", cascade="all", back_populates="post")

  # Set up constructor for the model
  def __init__(self, name):
    self.name = name