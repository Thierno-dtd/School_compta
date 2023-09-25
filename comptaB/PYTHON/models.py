from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name= db.Column(db.String(100))
    surname= db.Column(db.String(100))
    password = db.Column(db.String(100))
    
    
class Ecole(db.Model):
    __tablename__ = 'ecoles'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    eleveecole = db.relationship('Eleve',primaryjoin="Ecole.id == Eleve.idecole" , backref = 'ecoles', lazy = True)
    classecole = db.relationship('Classes',primaryjoin="Ecole.id == Classes.idecole" , backref = 'ecoles', lazy = True)
    
    
    
class Eleve(db.Model):
    __tablename__ = 'eleves'
    id  = db.Column (db.Integer ,primary_key = True )
    name = db.Column(db.String )
    pname = db.Column(db.String)
    idecole = db.Column(db.Integer)

class Classes(db.Model):
    __tablename__='classes'
    id = db.Column(db.Integer, primary_key = True)
    niveau = db.Column(db.String)
    groupe = db.Column(db.String)
    idecole = db.Column(db.String)
    
    

    

class Paiement(db.Model):
    __tablename__ = 'paiements'
    id = db.Column(db.Integer, primary_key=True)
    eleve_id = db.Column(db.Integer, db.ForeignKey('eleves.id'), nullable=False)
    montant = db.Column(db.Float, nullable=False)
    date_paiement = db.Column(db.Date, nullable=False)


class Annee(db.Model):
    __tablename__="annees"
    id = db.Column (db.Integer, primary_key = True)
    annee = db.COlumn(db.DateTime)
    
    
    
class Sequence(db.Model):
    __tablename__ ='sequences'
    id = db.Column (db.Integer, primary_key = True)
    type = db.Column(db.String)
    
