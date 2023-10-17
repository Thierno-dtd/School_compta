from urllib.parse import quote_plus
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

from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name= db.Column(db.String(100), nullable = False)
    surname= db.Column(db.String(100))
    password = db.Column(db.String(100))
    
    

    
class Ecole(db.Model):
    __tablename__ = 'ecoles'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    classecoleecole = db.relationship('EcoleClasse',primaryjoin="Ecole.id == EcoleClasse.ecole_id" , backref = 'ecoles', lazy = True)
  

class Classe(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    
    # Relation entre Classe et Eleve
    EcoleClasseclasse = db.relationship('EcoleClasse', backref='classes', lazy=True)
    
    
    # Relation entre Classe et FraisScolarite

class Eleve(db.Model):
    __tablename__ = 'eleves'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    
    paiements = db.relationship('Paiement', backref='eleve', lazy=True)
    eleveclass = db.relationship('EleveClasse', backref='eleve', lazy=True)

class EcoleClasse(db.Model):
    __tablename__ = 'ecoleclasse'
    id = db.Column(db.Integer, primary_key=True)
    ecole_id = db.Column(db.Integer, db.ForeignKey('ecoles.id'), nullable=False)
    classe_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    annee = db.Column(db.String(15), nullable = False)
    montant = db.Column(db.Float, nullable=False)
    paiements = db.relationship('Paiement', backref='ecoleclasse', lazy=True)
    eleveclass = db.relationship('EleveClasse', backref='ecoleclasse', lazy=True)
   

class Paiement(db.Model):
    __tablename__ = 'paiements'
    id = db.Column(db.Integer, primary_key=True)
    montant = db.Column(db.Float, nullable=False)
    
    # Clé étrangère pour lier un paiement à un élève
    eleve_id = db.Column(db.Integer, db.ForeignKey('eleves.id'), nullable=False)
    
    # Clé étrangère pour lier un paiement à une classe
    EcoleClassepaiement = db.Column(db.Integer, db.ForeignKey('ecoleclasse.id'), nullable=False)
    
    
class EleveClasse(db.Model):
    __tablename__ = "eleveclasses"
    id = db.Column(db.Integer, primary_key=True)
    ecoleclasse_id = db.Column(db.Integer, db.ForeignKey('ecoleclasse.id'), nullable = False)
    eleve_id = db.Column(db.Integer, db.ForeignKey('eleves.id'), nullable = False)
    
    
 
    
    

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)
