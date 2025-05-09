from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app.models.models import Utilisateur, Etablissement, Categorie, Avis, Possede

main = Blueprint('main', __name__)

# --- ETABLISSEMENTS ---

# Page d'accueil affichant la carte avec tous les établissements
@main.route("/")
def home():
    etablissements = Etablissement.get_all_json()
    return render_template("map.html", etablissements=etablissements)

# Récupère tous les établissements (format JSON si besoin)
@main.route("/etablissements", methods=["GET"])
def get_etablissements():
    return jsonify(Etablissement.get_all_json())

# Récupère un établissement par son identifiant (format JSON)
@main.route("/etablissement/<idetab>", methods=["GET"])
def get_etablissement(idetab):
    return jsonify(Etablissement.get_by_id_json(idetab))

# ----------- CREATE -----------

# Formulaire HTML pour ajouter un établissement
@main.route("/etablissement/ajouter", methods=["GET"])
def etablissement_ajouter_form():
    return render_template("ajouter_etablissement.html")

# Traitement POST du formulaire d’ajout
@main.route("/etablissement/ajouter", methods=["POST"])
def ajouter_etablissement():
    data = request.form
    Etablissement.create_from_json(data)
    return redirect(url_for("main.home"))

# ----------- UPDATE -----------

# Formulaire HTML de modification
@main.route("/etablissement/modifier/<idetab>", methods=["GET"])
def modifier_etablissement_form(idetab):
    etab = Etablissement.query.get_or_404(idetab)
    return render_template("modifier_etablissement.html", etab=etab)

# Traitement POST du formulaire de modification
@main.route("/etablissement/modifier/<idetab>", methods=["POST"])
def modifier_etablissement(idetab):
    data = request.form
    Etablissement.update_from_json(idetab, data)
    return redirect(url_for("main.home"))

# ----------- DELETE -----------

# Formulaire HTML de confirmation de suppression
@main.route("/etablissement/supprimer/<idetab>", methods=["GET"])
def supprimer_etablissement_form(idetab):
    etab = Etablissement.query.get_or_404(idetab)
    return render_template("supprimer_etablissement.html", etab=etab)

# Traitement POST de la suppression (form HTML natif)
@main.route("/etablissement/supprimer/<idetab>", methods=["POST"])
def supprimer_etablissement(idetab):
    Etablissement.delete_by_id(idetab)
    return redirect(url_for("main.home"))

# --- UTILISATEURS ---

# Affiche la liste de tous les utilisateurs
@main.route("/utilisateurs", methods=["GET"])
def get_utilisateurs():
    return jsonify(Utilisateur.get_all_json())

# Affiche un utilisateur spécifique par son identifiant
@main.route("/utilisateur/<iduser>", methods=["GET"])
def get_utilisateur(iduser):
    return jsonify(Utilisateur.get_by_id_json(iduser))

# Affiche le formulaire pour ajouter un nouvel utilisateur
@main.route("/utilisateur/ajouter", methods=["GET"])
def utilisateur_ajouter_form():
    return render_template("ajouter_utilisateur.html")

# Traite le formulaire pour ajouter un nouvel utilisateur                              FAUT RENVOYER SUR UNE PAGE D'AUTHENTIFICATION
@main.route("/utilisateur/ajouter", methods=["POST"])
def ajouter_utilisateur():
    data = request.form
    return jsonify(Utilisateur.create_from_json(data)), 201

# Affiche le formulaire pour modifier un utilisateur existant
@main.route("/utilisateur/modifier/<iduser>", methods=["GET"])
def utilisateur_modifier_form(iduser):
    utilisateur = Utilisateur.get_by_id_json(iduser)
    return render_template("modifier_utilisateur.html", utilisateur=utilisateur)

# Traite le formulaire pour modifier un utilisateur                                    FAUT RENVOYER SUR UNE PAGE map
@main.route("/utilisateur/modifier/<iduser>", methods=["POST"])                       
def modifier_utilisateur(iduser):
    data = request.form
    return jsonify(Utilisateur.update_from_json(iduser, data))

# Affiche la page de confirmation pour supprimer un utilisateur                        FAUT RENVOYER SUR UNE PAGE
@main.route("/utilisateur/supprimer/<iduser>", methods=["GET"])                         
def utilisateur_supprimer_form(iduser):
    utilisateur = Utilisateur.get_by_id_json(iduser)
    return render_template("supprimer_utilisateur.html", utilisateur=utilisateur)

# Traite la suppression d'un utilisateur
@main.route("/utilisateur/supprimer/<iduser>", methods=["POST"])
def supprimer_utilisateur(iduser):
    return jsonify(Utilisateur.delete_by_id(iduser))


# --- CATEGORIES ---

# Affiche la liste de toutes les catégories (format JSON)
@main.route("/categories", methods=["GET"])
def get_categories():
    return jsonify(Categorie.get_all_json())

# Affiche une catégorie spécifique par son identifiant (format JSON)
@main.route("/categorie/<idcat>", methods=["GET"])
def get_categorie(idcat):
    return jsonify(Categorie.get_by_id_json(idcat))

# Affiche le formulaire pour ajouter une nouvelle catégorie
@main.route("/categorie/ajouter", methods=["GET"])
def categorie_ajouter_form():
    return render_template("ajouter_categorie.html")

# Traite le formulaire pour ajouter une nouvelle catégorie
@main.route("/categorie/ajouter", methods=["POST"])
def ajouter_categorie():
    data = request.form
    return jsonify(Categorie.create_from_json(data)), 201

# Affiche le formulaire pour modifier une catégorie existante
@main.route("/categorie/modifier/<idcat>", methods=["GET"])
def categorie_modifier_form(idcat):
    categorie = Categorie.get_by_id_json(idcat)
    return render_template("modifier_categorie.html", categorie=categorie)

# Traite le formulaire pour modifier une catégorie                                                  FAUT RENVOYER SUR UNE PAGE                       
@main.route("/categorie/modifier/<idcat>", methods=["POST"])
def modifier_categorie(idcat):
    data = request.form
    return jsonify(Categorie.update_from_json(idcat, data))

# Affiche la page de confirmation pour supprimer une catégorie
@main.route("/categorie/supprimer/<idcat>", methods=["GET"])
def categorie_supprimer_form(idcat):
    categorie = Categorie.get_by_id_json(idcat)
    return render_template("supprimer_categorie.html", categorie=categorie)

# Traite la suppression d'une catégorie                                                            FAUT RENVOYER SUR UNE PAGE 
@main.route("/categorie/supprimer/<idcat>", methods=["POST"])
def supprimer_categorie(idcat):
    return jsonify(Categorie.delete_by_id(idcat))


# --- AVIS ---

# Récupère la liste de tous les avis (format JSON)
@main.route("/avis", methods=["GET"])
def get_avis():
    return jsonify(Avis.get_all_json())

# Récupère un avis par son identifiant (format JSON)
@main.route("/avis/<idav>", methods=["GET"])
def get_avis_by_id(idav):
    return jsonify(Avis.get_by_id_json(idav))

# Affiche le formulaire pour ajouter un nouvel avis (méthode GET)
@main.route("/avis/ajouter", methods=["GET"])
def ajouter_avis_form():
    return render_template('ajouter_avis.html')

# Ajoute un nouvel avis à la base de données (méthode POST)
@main.route("/avis/ajouter", methods=["POST"])
def ajouter_avis():
    data = request.form.to_dict()  # on utilise form pour obtenir les données du formulaire
    return jsonify(Avis.create_from_json(data)), 201

# Affiche le formulaire pour modifier un avis (méthode GET)
@main.route("/avis/modifier/<idav>", methods=["GET"])
def modifier_avis_form(idav):
    avis = Avis.get_by_id_json(idav)
    return render_template('modifier_avis.html', avis=avis)

# Modifie un avis existant via son identifiant (méthode PUT)
@main.route("/avis/modifier/<idav>", methods=["POST"])
def modifier_avis(idav):
    data = request.form.to_dict()  # on récupère les données du formulaire
    return jsonify(Avis.update_from_json(idav, data))

# Supprime un avis via son identifiant (méthode DELETE)
@main.route("/avis/supprimer/<idav>", methods=["GET"])
def supprimer_avis_form(idav):
    avis = Avis.get_by_id_json(idav)
    return render_template('supprimer_avis.html', avis=avis)

@main.route("/avis/supprimer/<idav>", methods=["POST"])
def supprimer_avis(idav):
    return jsonify(Avis.delete_by_id(idav))


# --- POSSEDE ---

# Récupère la liste de toutes les relations Possede (format JSON)
@main.route("/possede", methods=["GET"])
def get_possedes():
    return jsonify(Possede.get_all_json())

# Récupère une relation Possede par idcat et idetab (format JSON)
@main.route("/possede/<idcat>/<idetab>", methods=["GET"])
def get_possede(idcat, idetab):
    return jsonify(Possede.get_by_id_json(idcat, idetab))

# Affiche le formulaire pour ajouter une nouvelle relation Possede
@main.route("/possede/ajouter", methods=["GET"])
def possede_ajouter_form():
    categories = Categorie.get_all_json()  # Liste des catégories
    etablissements = Etablissement.get_all_json()  # Liste des établissements
    return render_template("ajouter_possede.html", categories=categories, etablissements=etablissements)

# Ajoute une nouvelle relation Possede à la base de données
@main.route("/possede/ajouter", methods=["POST"])
def ajouter_possede():
    data = request.form  # Récupère les données du formulaire
    Possede.create_from_json(data)  # Crée la relation Possede
    return redirect(url_for("main.home"))  # Redirige vers la page d'accueil

# Affiche le formulaire de confirmation pour supprimer une relation Possede
@main.route("/possede/supprimer/<idcat>/<idetab>", methods=["GET"])
def possede_supprimer_form(idcat, idetab):
    possede = Possede.get_by_id_json(idcat, idetab)  # Récupère la relation à supprimer
    return render_template("supprimer_possede.html", possede=possede)

# Supprime une relation Possede via idcat et idetab
@main.route("/possede/supprimer/<idcat>/<idetab>", methods=["POST"])
def supprimer_possede(idcat, idetab):
    Possede.delete_by_id(idcat, idetab)  # Supprime la relation
    return redirect(url_for("main.home"))  # Redirige vers la page d'accueil

# Supprime une relation Possede via idcat et idetab (format JSON)
@main.route("/possede/supprimer/<idcat>/<idetab>", methods=["DELETE"])
def supprimer_possede_json(idcat, idetab):
    return jsonify(Possede.delete_by_id(idcat, idetab))

# Affiche le formulaire pour modifier une relation Possede
@main.route("/possede/modifier/<idcat>/<idetab>", methods=["GET"])
def possede_modifier_form(idcat, idetab):
    possede = Possede.get_by_id_json(idcat, idetab)  # Récupère la relation à modifier
    categories = Categorie.get_all_json()  # Liste des catégories
    etablissements = Etablissement.get_all_json()  # Liste des établissements
    return render_template("modifier_possede.html", possede=possede, categories=categories, etablissements=etablissements)

# Modifie une relation Possede existante
@main.route("/possede/modifier/<idcat>/<idetab>", methods=["POST"])
def modifier_possede(idcat, idetab):
    data = request.form  # Récupère les données du formulaire
    possede = Possede.query.get_or_404((idcat, idetab))  # Récupère la relation existante
    Possede.update_from_form(possede, data)  # Met à jour la relation
    return redirect(url_for("main.home"))  # Redirige vers la page d'accueil
