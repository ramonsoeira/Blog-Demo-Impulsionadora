from flask import Flask


def init_app(app: Flask):
    from .auth_view import bp as bp_auth

    app.register_blueprint(bp_auth, url_prefix="/auth")

    from .home_view import bp as bp_home

    app.register_blueprint(bp_home, url_prefix="/home")
