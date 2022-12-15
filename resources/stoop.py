from flask_restful import Resource
from flask import request
from models.stoop import Stoop
from models.db import db
from sqlalchemy.orm import joinedload

class Stoops(Resource):
  # def get(self):
  #   stoops = Stoop.find_all()
  #   return [s.json() for s in stoops]

  def get(self):
    stoops = Stoop.query.options(joinedload('neighborhood')).all()
    return [{**s.json(), "neighborhood": s.neighborhood.json()} for s in stoops]

  def post(self):
    data = request.get_json()
    stoop = Stoop(**data)
    stoop.create()
    return stoop.json(), 201

class StoopDetails(Resource):
  def get(self, stoop_id):
    data = Stoop.find_by_id(stoop_id)
    result = data.json()
    return result

  def delete(self, stoop_id):
    data = Stoop.delete(stoop_id)
    return data

  def put(self, stoop_id):
    data = Stoop.update(stoop_id)
    return data