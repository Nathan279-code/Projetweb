from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from app import db
from app.models.models import Utilisateur, Etablissement, Categorie, Avis, Possede
import json

main = Blueprint('main', __name__)

#  PAGE DE LA CARTE
@main.route("/")
def home():
    etablissements = Etablissement.query.all()
    etablissements_json = []
    for e in etablissements:
        etablissements_json.append({
            "id": e.idetab,
            "nom": e.nometab,
            "adresse": e.adetab,
            "ville": e.villeetab,
            "cp": e.cpetab,
            "latitude": 45.7597,  
            "longitude": 4.8422  
        })
    return render_template("map.html", etablissements=etablissements_json) 


#  TOUS LES ETABLISSEMENTS (JSON)
@main.route("/etablissements", methods=["GET"])
def get_etablissements():
    etablissements = Etablissement.query.all()
    resultat = []
    for e in etablissements:
        resultat.append({
            "id": e.idetab,
            "nom": e.nometab,
            "adresse": e.adetab,
            "ville": e.villeetab,
            "cp": e.cpetab,
            "tel": e.teletab,
            "siteweb": e.sitewebetab,
            "idcat": e.idcat
        })
    return jsonify(resultat)


#  ETABLISSEMENT PAR ID
@main.route("/etablissement/<idetab>", methods=["GET"])
def get_etablissement(idetab):
    e = Etablissement.query.get_or_404(idetab)
    return jsonify({
        "id": e.idetab,
        "nom": e.nometab,
        "adresse": e.adetab,
        "ville": e.villeetab,
        "cp": e.cpetab,
        "tel": e.teletab,
        "siteweb": e.sitewebetab,
        "idcat": e.idcat
    })


#  AJOUTER UN ETABLISSEMENT
@main.route("/ajouter_etablissement", methods=["POST"])
def ajouter_etablissement():
    data = request.json
    etab = Etablissement(
        idetab=data["idetab"],
        nometab=data["nometab"],
        adetab=data["adetab"],
        villeetab=data["villeetab"],
        cpetab=data["cpetab"],
        teletab=data["teletab"],
        sitewebetab=data["sitewebetab"],
        idcat=data["idcat"]
    )
    db.session.add(etab)
    db.session.commit()
    return jsonify({"message": "Etablissement ajouté"}), 201


#  MODIFIER UN ETABLISSEMENT
@main.route("/modifier_etablissement/<idetab>", methods=["PUT"])
def modifier_etablissement(idetab):
    etab = Etablissement.query.get_or_404(idetab)
    data = request.json
    etab.nometab = data.get("nometab", etab.nometab)
    etab.adetab = data.get("adetab", etab.adetab)
    etab.villeetab = data.get("villeetab", etab.villeetab)
    etab.cpetab = data.get("cpetab", etab.cpetab)
    etab.teletab = data.get("teletab", etab.teletab)
    etab.sitewebetab = data.get("sitewebetab", etab.sitewebetab)
    etab.idcat = data.get("idcat", etab.idcat)
    db.session.commit()
    return jsonify({"message": "Etablissement modifié"})


#  SUPPRIMER UN ETABLISSEMENT
@main.route("/supprimer_etablissement/<idetab>", methods=["DELETE"])
def supprimer_etablissement(idetab):
    etab = Etablissement.query.get_or_404(idetab)
    db.session.delete(etab)
    db.session.commit()
    return jsonify({"message": "Etablissement supprimé"})


#  AJOUTER UN UTILISATEUR
@main.route("/ajouter_utilisateur", methods=["POST"])
def ajouter_utilisateur():
    data = request.json
    user = Utilisateur(
        iduser=data["iduser"],
        username=data["username"],
        emailuser=data["emailuser"],
        mdpuser=data["mdpuser"],
        admin=data["admin"]
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Utilisateur ajouté"}), 201

# READ TOUT LES UTILISATEUR
@main.route("/utilisateurs", methods=["GET"])
def get_utilisateurs():
    utilisateurs = Utilisateur.query.all()
    resultat = []
    for user in utilisateurs:
        resultat.append({
            "iduser": user.iduser,
            "username": user.username,
            "emailuser": user.emailuser,
            "mdpuser": user.mdpuser,
            "admin": user.admin
        })
    return jsonify(resultat)

#READ 1 USER SELON SONT ID
@main.route("/utilisateur/<iduser>", methods=["GET"])
def get_utilisateur(iduser):
    user = Utilisateur.query.get_or_404(iduser)
    return jsonify({
        "iduser": user.iduser,
        "username": user.username,
        "emailuser": user.emailuser,
        "mdpuser": user.mdpuser,
        "admin": user.admin
    })

#UPDATE UN USER
@main.route("/modifier_utilisateur/<iduser>", methods=["PUT"])
def modifier_utilisateur(iduser):
    user = Utilisateur.query.get_or_404(iduser)
    data = request.json
    user.username = data.get("username", user.username)
    user.emailuser = data.get("emailuser", user.emailuser)
    user.mdpuser = data.get("mdpuser", user.mdpuser)
    user.admin = data.get("admin", user.admin)
    db.session.commit()
    return jsonify({"message": "Utilisateur modifié"})


#DELET UN USER SELON ID
@main.route("/supprimer_utilisateur/<iduser>", methods=["DELETE"])
def supprimer_utilisateur(iduser):
    user = Utilisateur.query.get_or_404(iduser)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Utilisateur supprimé"})





























#  AJOUTER UNE CATÉGORIE
@main.route("/ajouter_categorie", methods=["POST"])
def ajouter_categorie():
    data = request.json
    cat = Categorie(
        idcat=data["idcat"],
        nomcat=data["nomcat"]
    )
    db.session.add(cat)
    db.session.commit()
    return jsonify({"message": "Catégorie ajoutée"}), 201


#  AJOUTER UN AVIS
@main.route("/ajouter_avis", methods=["POST"])
def ajouter_avis():
    data = request.json
    avis = Avis(
        idav=data["idav"],
        note=data["note"],
        commentaire=data["commentaire"],
        datecreation=data["datecreation"],
        iduser_Utilisateur=data["iduser"],
        idetab_Etablissement=data["idetab"]
    )
    db.session.add(avis)
    db.session.commit()
    return jsonify({"message": "Avis ajouté"}), 201


#  LIER UNE CATÉGORIE À UN ÉTABLISSEMENT
@main.route("/lier_categorie", methods=["POST"])
def lier_categorie():
    data = request.json
    possede = Possede(
        idcat=data["idcat"],
        idetab=data["idetab"]
    )
    db.session.add(possede)
    db.session.commit()
    return jsonify({"message": "Lien catégorie/établissement ajouté"}), 201

@main.route("/ajouter_etablissement_form", methods=["POST"])
def ajouter_etablissement_form():
    idetab = request.form["idetab"]
    nometab = request.form["nometab"]
    adetab = request.form["adetab"]
    villeetab = request.form["villeetab"]
    cpetab = request.form["cpetab"]
    teletab = request.form["teletab"]
    sitewebetab = request.form["sitewebetab"]
    idcat = request.form["idcat"]

    etab = Etablissement(
        idetab=idetab,
        nometab=nometab,
        adetab=adetab,
        villeetab=villeetab,
        cpetab=cpetab,
        teletab=teletab,
        sitewebetab=sitewebetab,
        idcat=idcat
    )
    db.session.add(etab)
    db.session.commit()
    return redirect(url_for("main.home"))  # Redirige vers la carte après l'ajout
