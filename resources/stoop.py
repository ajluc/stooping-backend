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