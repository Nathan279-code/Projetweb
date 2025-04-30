from app import db

class Utilisateur(db.Model):
    iduser = db.Column(db.String(6), primary_key=True)
    username = db.Column(db.String(6), nullable=False)
    emailuser = db.Column(db.String(90), nullable=False)
    mdpuser = db.Column(db.String(90), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    avis = db.relationship("Avis", backref="utilisateur", lazy=True)
    

class Etablissement(db.Model):
    idetab = db.Column(db.String(6), primary_key=True)
    nometab = db.Column(db.String(30), nullable=False)
    adetab = db.Column(db.String(80), nullable=False)
    villeetab = db.Column(db.String(40), nullable=False)
    cpetab = db.Column(db.String(8), nullable=False)
    teletab = db.Column(db.String(15), nullable=False)
    sitewebetab = db.Column(db.String(80), nullable=False)
    idcat = db.Column(db.String(6), nullable=False)

    avis = db.relationship("Avis", backref="etablissement", lazy=True)
    categories = db.relationship("Possede", back_populates="etablissement")

















class Categorie(db.Model):
    idcat = db.Column(db.String(6), primary_key=True)
    nomcat = db.Column(db.String(30), nullable=False)

    etablissements = db.relationship("Possede", back_populates="categorie")


class Avis(db.Model):
    idav = db.Column(db.String(6), primary_key=True)
    note = db.Column(db.Float, nullable=False)
    commentaire = db.Column(db.String(200), nullable=False)
    datecreation = db.Column(db.Date, nullable=False)

    iduser_Utilisateur = db.Column(db.String(6), db.ForeignKey("utilisateur.iduser"))
    idetab_Etablissement = db.Column(db.String(6), db.ForeignKey("etablissement.idetab"))


class Possede(db.Model):
    idcat = db.Column(db.String(6), db.ForeignKey("categorie.idcat"), primary_key=True)
    idetab = db.Column(db.String(6), db.ForeignKey("etablissement.idetab"), primary_key=True)

    categorie = db.relationship("Categorie", back_populates="etablissements")
    etablissement = db.relationship("Etablissement", back_populates="categories")
