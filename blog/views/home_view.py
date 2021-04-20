from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint("home", __name__)


@bp.route("/", methods=["GET"])
@login_required
def home_render():
    return render_template("home.html")


# belezinha