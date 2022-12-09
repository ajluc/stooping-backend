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
  users = db.relationship("User", cascade="all", back_populates="neighborhood")
  stoops = db.relationship("Stoop", cascade="all", back_populates="neighborhood")

  # Set up constructor for the model
  def __init__(self, name):
    self.name = name

  def json(self):
    return {"id": self.id, "name": self.name, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

  def create(self):
    db.session.add(self)
    db.session.commit()
    return self

  @classmethod
  def find_all(cls):
    return Neighborhood.query.all()

  @classmethod
  def find_by_id(cls, neighborhood_id):
    neighborhood = Neighborhood.query.filter_by(id=neighborhood_id).first()
    return neighborhood