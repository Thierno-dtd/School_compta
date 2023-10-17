from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from .models import Ecole, EcoleClasse, EleveClasse



main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("home.html")


@main.route('/dashboard')
def dashboard():
    # Logique pour générer la page de tableau de bord (remplacez ceci par votre propre logique)
    return render_template('ecoles.html')


@main.route('/classe/<int:id>')
def classe(id):
    # Logique pour générer la page de la classe (remplacez ceci par votre propre logique)
    return render_template('index.html')



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


@main.route('/ShowEleve')
@login_required
def show_eleve():
    classe_id = int(request.form.get('idClasse'))
    ann = request.form.get('annee')
    id_ecole_classe = EcoleClasse.query.filter_by(classe_id = classe_id, annee = ann ).first()
    if not id_ecole_classe :
        return render_template('index.html')
    all_eleve = EleveClasse.query.filter_by(ecoleclasse_id = id_ecole_classe )
    return render_template('showeleve.html', data = all_eleve)


    
    
    

