from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_user
from werkzeug.exceptions import NotFound

from blog.forms.auth_form import LoginForm
from blog.models.user_model import UserModel

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = request.form.get("email")
        password = request.form.get("password")
        rememberme = request.form.get("rememberme")
        found_user: UserModel = UserModel.query.filter_by(email=email)
        if not found_user or password != found_user.password:
            raise NotFound("Email or password are not correct")
        login_user(found_user, rememberme)

        next_access: str = request.args.get("next")
        if not next_access or next_access.startswith("/"):
            next_access = "home.home_render"
        return redirect(url_for(next_access))
    return render_template("login.html", form=form)


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

    session = current_app.db.session

    name = request.form.get("name")
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    new_user = UserModel(name=name, username=username, email=email, password=password)
    session.add(new_user)
    session.commit()

    return redirect(url_for("home.home_render"))
