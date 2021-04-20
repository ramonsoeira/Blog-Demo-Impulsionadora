from flask import Flask
from flask_login import LoginManager

from blog.models.user_model import UserModel


def init_app(app: Flask):
    login_manager = LoginManager(app)

    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def user_loader(user_id):
        return UserModel.query.get(user_id)
