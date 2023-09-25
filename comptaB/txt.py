from urllib.parse import quote_plus
#importation de flask
from flask import Flask,render_template,request,redirect

#importation de flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

#Demarrage de l'apk
app = Flask(__name__)

#Chaîne de connexion à la base de donnée
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eCom.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#masquer les notifications

#creation de l'intance de la BD
db = SQLAlchemy(app)

from flask_login import UserMixin

class Opera(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    ad = db.Column(db.Integer)
    passe = db.relationship('Pera', backref = 'opera', lazy = True)
    
    
class Pera(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    no = db.Column(db.Integer)
    idecole = db.Column(db.Integer, db.ForeignKey('opera.id'), nullable = False )

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    new = Pera(no = 25)
    db.session.add(new)
    db.session.commit()
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)
