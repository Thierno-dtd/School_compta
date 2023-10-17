from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name= db.Column(db.String(100), nullable = False)
    surname= db.Column(db.String(100))
    password = db.Column(db.String(100))
    
    
"""class Ecole(db.Model):
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
    idecole = db.Column(db.Integer, db.ForeignKey('ecoles.id'))

class Classes(db.Model):
    __tablename__='classes'
    id = db.Column(db.Integer, primary_key = True)
    niveau = db.Column(db.String)
    groupe = db.Column(db.String)
    idecole = db.Column(db.Integer, db.ForeignKey('ecoles.id'))
    
    

    

class Paiement(db.Model):
    __tablename__ = 'paiements'
    id = db.Column(db.Integer, primary_key=True)
    eleve_id = db.Column(db.Integer, db.ForeignKey('eleves.id'), nullable=False)
    montant = db.Column(db.Float, nullable=False)
    date_paiement = db.Column(db.Date, nullable=False)


class Annee(db.Model):
    __tablename__="annees"
    id = db.Column (db.Integer, primary_key = True)
    annee = db.Column(db.DateTime)
    
    
    
    
class Sequence(db.Model):
    __tablename__ ='sequences'
    id = db.Column (db.Integer, primary_key = True)
    type = db.Column(db.String)
    






class Annee(db.Model):
    __tablename__ = 'annees'
    id = db.Column(db.Integer, primary_key=True)
    annee_academique = db.Column(db.String(100), nullable=False, unique=True)
    
    # Relation entre Annee et Paiement
    paiements = db.relationship('Paiement', backref='annee', lazy=True)
    scolar = db.relationship('FraisScolarite', backref='annee', lazy=True)
 """   
    
class Ecole(db.Model):
    __tablename__ = 'ecoles'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    classecoleecole = db.relationship('EcoleClasse',primaryjoin="Ecole.id == EcoleClasse.ecole_id" , backref = 'ecoles', lazy = True)
  
  
  
class Annee(db.Model):
    __tablename__ = 'annees'
    id = db.Column(db.Integer, primary_key=True)
    annee = db.Column(db.String(8), nullable=False)
    anneeclassecoleecole = db.relationship('EcoleClasse',primaryjoin="Annee.id == EcoleClasse.annee" , backref = 'annees', lazy = True)
    

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
    annee = db.Column(db.Integer, db.ForeignKey('annees.id'), nullable=False)
    
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
    