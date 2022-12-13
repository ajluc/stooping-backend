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
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  neighborhood_id = db.Column(db.Integer, db.ForeignKey('neighborhoods.id'), nullable=False)
  user = db.relationship("User", back_populates="stoops")
  neighborhood = db.relationship("Neighborhood", back_populates="stoops")
  latitude = db.Column(db.Float, nullable=True)
  longitude = db.Column(db.Float, nullable=True)

  # Set up constructor for the model
  def __init__(self, title, description, image, user_id, neighborhood_id, latitude, longitude):
    self.title = title
    self.description = description
    self.image = image
    self.user_id = user_id
    self.neighborhood_id = neighborhood_id
    self.latitude = latitude
    self.longitude = longitude

  def json(self):
    return {"id": self.id, "title": self.title, "description": self.description, "image": self.image, "latitude": self.latitude, "longitude": self.longitude, "user_id": self.user_id, "neighborhood_id": self.neighborhood_id, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

  def create(self):
    db.session.add(self)
    db.session.commit()
    return self

  @classmethod
  def find_all(cls):
    return Stoop.query.all()

  @classmethod
  def find_by_id(cls, stoop_id):
    stoop = Stoop.query.filter_by(id=stoop_id).first()
    return stoop

