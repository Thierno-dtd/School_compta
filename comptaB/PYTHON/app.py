"""from urllib.parse import quote_plus
#importation de flask
from flask import Flask,render_template,request,redirect

#importation de flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

#Demarrage de l'apk
app = Flask(__name__)

#Chaîne de connexion à la base de donnée
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/dbcomptab'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#masquer les notifications

#creation de l'intance de la BD
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("home.html")

@app.route('/dashboard')
def dashboard():
    # Logique pour générer la page de tableau de bord (remplacez ceci par votre propre logique)
    return render_template('ecoles.html')

@app.route('/classe/<int:id>')
def classe(id):
    # Logique pour générer la page de la classe (remplacez ceci par votre propre logique)
    return render_template('classe.html', id=id)

if __name__ == '__main__':
    app.run(debug=True)"""
