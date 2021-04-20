from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField, StringField
from flask_wtf.html5 import EmailInput


class LoginForm(FlaskForm):
    email = StringField("email")
    password = PasswordField("password")
    remeberme = BooleanField("remember-me")

    submit = SubmitField("login")
