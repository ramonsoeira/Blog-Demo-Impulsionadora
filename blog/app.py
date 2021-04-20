from flask import Flask
from os import getenv

from blog.configurations import database
from blog.configurations import migration
from blog.configurations import authentication
from blog import views


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = getenv("SECRET_KEY")

    database.init_app(app)
    migration.init_app(app)
    authentication.init_app(app)
    views.init_app(app)

    return app
