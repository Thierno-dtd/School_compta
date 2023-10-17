from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import Ecole, EcoleClasse, Eleve, Paiement, User
from . import db
import pandas as pd

auth = Blueprint('auth', __name__)

global ch_id_ecole, ch_id_classe

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))


    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    name = request.form.get('name')
    pname = request.form.get('pname')
    password = request.form.get('password')
    passwordOK = request.form.get('passwordOK')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    if password != passwordOK:
        flash('Your confirm password is different')
        return redirect(url_for('auth.signup'))
    if len(name) <3 or len(pname) <3:
        flash('The first and last names must exceed 2 caracters')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), pname=pname)


    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/main/AddEleve', methods=['POST'])
@login_required
def choix_ecole_classe():
    ch_id_ecole = request.form.get('checole')
    ch_id_classe = request.form.get('chclasse')
    



@auth.route('/main/AddEleve', methods=['POST'])
@login_required
def import_csv():
    if 'file' not in request.files:
        return "Aucun fichier n'a été téléchargé."

    file = request.files['file']

    if file.filename == '':
        return "Aucun fichier n'a été sélectionné."

    if not file.filename.endswith('.csv'):
        return "Le fichier doit avoir l'extension .csv."

    if file:
        try:
            df = pd.read_csv(file)
            expected_columns = ['nom', 'prenom', 'age']  # Définissez les colonnes attendues
            if not set(expected_columns).issubset(df.columns):
                return "Le fichier CSV doit contenir les colonnes nom, prenom et age."

            # Parcourir les lignes du dataframe et créer des instances Etudiant
            for index, row in df.iterrows():
                etudiant = Eleve(nom=row['nom'], prenom=row['prenom'])
                db.session.add(etudiant)

            # Effectuer un commit pour enregistrer les étudiants dans la base de données
            db.session.commit()

            return "Les étudiants ont été importés avec succès depuis le fichier CSV."
        except pd.errors.ParserError:
            return "Le fichier CSV est mal formaté."
    if 'file' not in request.files:
        return "Aucun fichier n'a été téléchargé."

    file = request.files['file']

    if file.filename == '':
        return "Aucun fichier n'a été sélectionné."

    if file:
        # Lire le fichier CSV avec pandas
        df = pd.read_csv(file)

        # Parcourir les lignes du dataframe et créer des instances Etudiant
        for index, row in df.iterrows():
            eleve = Eleve(nom=row['nom'], prenom=row['prenom'], age=row['age'])
            db.session.add(eleve)

        # Effectuer un commit pour enregistrer les étudiants dans la base de données
        db.session.commit()

        return "Les étudiants ont été importés avec succès depuis le fichier CSV."
    

@auth.route('/main/AddSchool', methods=['POST'])
@login_required
def createAll():
    nom = request.form.get('nomschool')
    nameschool = Ecole.query.filter_by(nom = nom).first()
    
    
    if  nameschool :
        flash('Le nom de l\'etablissement existe déja')
    
    if not nameschool:   
        new_school = Ecole(nom)
        db.session.add(new_school)
        db.session.commit()
        flash('Ajout reussi avec succès')    
        

@auth.route('/main/showStudent/<int:id>')
def payement(id):
    try : 
        p = float(request.form.get('price'))
    except ValueError:
        flash('Somme non acceptée')
        
    if p<=float(0) :
        flash('La somme saisi est négative/nulle')
    else : 
        annee = request.form.get('annee')
        class_id = request.form.get('idClasse')
        sommeT = EcoleClasse.query.filter_by(annee = annee,class_id = class_id ).first().montant
        if p <= sommeT:
            new_paie = Paiement()
        
        
    