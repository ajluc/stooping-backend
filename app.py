from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_migrate import Migrate
from models.db import db
from models.user import User
from models.stoop import Stoop
from models.neighborhood import Neighborhood
from resources import user, stoop, neighborhood

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/stooping_db"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(user.Users, '/users')
api.add_resource(neighborhood.Neighborhoods, '/nb')
api.add_resource(stoop.Stoops, '/stoops')

if __name__ == '__main__':
    app.run(debug=True)