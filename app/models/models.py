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

    def to_dict(self):
        return {
            "idcat": self.idcat,
            "nomcat": self.nomcat
        }

    @staticmethod
    def get_all_json():
        return [cat.to_dict() for cat in Categorie.query.all()]

    @staticmethod
    def get_by_id_json(idcat):
        cat = Categorie.query.get_or_404(idcat)
        return cat.to_dict()

    @staticmethod
    def create_from_json(data):
        cat = Categorie(
            idcat=data["idcat"],
            nomcat=data["nomcat"]
        )
        db.session.add(cat)
        db.session.commit()
        return cat.to_dict()

    @staticmethod
    def update_from_json(idcat, data):
        cat = Categorie.query.get_or_404(idcat)
        cat.nomcat = data.get("nomcat", cat.nomcat)
        db.session.commit()
        return cat.to_dict()

    @staticmethod
    def delete_by_id(idcat):
        cat = Categorie.query.get_or_404(idcat)
        db.session.delete(cat)
        db.session.commit()
        return {"message": "Catégorie supprimée"}


class Avis(db.Model):
    idav = db.Column(db.String(6), primary_key=True)
    note = db.Column(db.Float, nullable=False)
    commentaire = db.Column(db.String(200), nullable=False)
    datecreation = db.Column(db.Date, nullable=False)

    iduser_Utilisateur = db.Column(db.String(6), db.ForeignKey("utilisateur.iduser"))
    idetab_Etablissement = db.Column(db.String(6), db.ForeignKey("etablissement.idetab"))

    def to_dict(self):
        return {
            "idav": self.idav,
            "note": self.note,
            "commentaire": self.commentaire,
            "datecreation": self.datecreation.isoformat(),
            "iduser": self.iduser_Utilisateur,
            "idetab": self.idetab_Etablissement
        }

    @staticmethod
    def get_all_json():
        return [avis.to_dict() for avis in Avis.query.all()]

    @staticmethod
    def get_by_id_json(idav):
        avis = Avis.query.get_or_404(idav)
        return avis.to_dict()

    @staticmethod
    def create_from_json(data):
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
        return avis.to_dict()

    @staticmethod
    def update_from_json(idav, data):
        avis = Avis.query.get_or_404(idav)
        avis.note = data.get("note", avis.note)
        avis.commentaire = data.get("commentaire", avis.commentaire)
        avis.datecreation = data.get("datecreation", avis.datecreation)
        avis.iduser_Utilisateur = data.get("iduser", avis.iduser_Utilisateur)
        avis.idetab_Etablissement = data.get("idetab", avis.idetab_Etablissement)
        db.session.commit()
        return avis.to_dict()

    @staticmethod
    def delete_by_id(idav):
        avis = Avis.query.get_or_404(idav)
        db.session.delete(avis)
        db.session.commit()
        return {"message": "Avis supprimé"}


class Possede(db.Model):
    idcat = db.Column(db.String(6), db.ForeignKey("categorie.idcat"), primary_key=True)
    idetab = db.Column(db.String(6), db.ForeignKey("etablissement.idetab"), primary_key=True)

    categorie = db.relationship("Categorie", back_populates="etablissements")
    etablissement = db.relationship("Etablissement", back_populates="categories")

    def to_dict(self):
        return {
            "idcat": self.idcat,
            "idetab": self.idetab
        }

    @staticmethod
    def get_all_json():
        return [possede.to_dict() for possede in Possede.query.all()]

    @staticmethod
    def get_by_id_json(idcat, idetab):
        possede = Possede.query.get_or_404((idcat, idetab))
        return possede.to_dict()

    @staticmethod
    def create_from_json(data):
        possede = Possede(
            idcat=data["idcat"],
            idetab=data["idetab"]
        )
        db.session.add(possede)
        db.session.commit()
        return possede.to_dict()

    @staticmethod
    def delete_by_id(idcat, idetab):
        possede = Possede.query.get_or_404((idcat, idetab))
        db.session.delete(possede)
        db.session.commit()
        return {"message": "Relation supprimée"}
