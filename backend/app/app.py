import os

from flask import Flask
from flask_jwt_extended import JWTManager
from . import controllers

project_dir = os.path.dirname(os.path.abspath(__file__))


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config['JWT_SECRET_KEY'] = 'Super_Secret_JWT_KEY'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False

    JWTManager(app)

    app.register_blueprint(controllers.home.blueprint)
    app.register_blueprint(controllers.auth.blueprint)
    app.register_blueprint(controllers.account.blueprint)

    return app
