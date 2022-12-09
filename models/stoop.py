from models.db import db
from datetime import datetime

class Stoop(db.Model):
  # Define the table name
  __tablename__ = 'stoops'
  # Create the columns of the table
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255))
  description = db.Column(db.String(255))
  image = db.Column(db.Text)
  # reportedTaken = db.Column(db.ARRAY)
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())

  # Set up constructor for the model
  def __init__(self, title, description, image):
    self.title = title
    self.description = description
    self.image = image

