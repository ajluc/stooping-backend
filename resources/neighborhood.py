from flask_restful import Resource
from flask import request
from models.neighborhood import Neighborhood
from models.db import db
from sqlalchemy.orm import joinedload

class Neighborhoods(Resource):
  def get(self):
    neighborhoods = Neighborhood.find_all()
    return [n.json() for n in neighborhoods]

  def post(self):
    data = request.get_json()
    neighborhood = Neighborhood(**data)
    neighborhood.create()
    return neighborhood.json(), 201