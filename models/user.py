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
  neighborhood_id = db.Column(db.Integer, db.ForeignKey('neighborhoods.id'), nullable=True)
  neighborhood = db.relationship("Neighborhood", back_populates="users")
  stoops = db.relationship("Stoop", cascade="all", back_populates="user")


  # Set up constructor for the model
  def __init__(self, name, email, password_digest, neighborhood_id):
    self.name = name
    self.email = email
    self.password_digest = password_digest
    self.neighborhood_id = neighborhood_id

  def json(self):
    return {"id": self.id, "name": self.name, "email": self.email, "password_digest": self.password_digest,"neighborhood_id": self.neighborhood_id, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

  def create(self):
    db.session.add(self)
    db.session.commit()
    return self

  @classmethod
  def find_all(cls):
    return User.query.all()

  @classmethod
  def find_by_id(cls, user_id):
    user = User.query.filter_by(id=user_id).first()
    return user

  @classmethod
  def find_by_email(cls, email):
    user = User.query.filter_by(email=email).first()
    return user