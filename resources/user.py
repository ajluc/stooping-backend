from flask_restful import Resource
from flask import request
from models.user import User
from models.db import db
from sqlalchemy.orm import joinedload

class Users(Resource):
  def get(self):
    users = User.find_all()
    return [u.json() for u in users]

  def post(self):
    data = request.get_json()
    user = User(**data)
    user.create()
    return user.json(), 201

class UserDetails(Resource):
  def get(self, user_id):
    user = User.query.options(joinedload(
        'stoops')).filter_by(id=user_id).first()
    stoops = [s.json() for s in user.stoops]
    return {**user.json(), 'stoops': stoops}