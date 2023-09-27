from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from comptaB.PYTHON.models import Ecole

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html", users=current_user)


@main.route("/Njour")
@login_required
def non_paye():
    necole = int(request.form.get("ch_id_ecole"))


@main.route("/ecole")
@login_required
def n_ecole():
    all_ecole = Ecole.query.All()
    return render_template("pecole.html", data = all_ecole)



