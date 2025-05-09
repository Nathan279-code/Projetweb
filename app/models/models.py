from app import db

class Utilisateur(db.Model):
    iduser = db.Column(db.String(6), primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    emailuser = db.Column(db.String(90), nullable=False)
    mdpuser = db.Column(db.String(90), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    avis = db.relationship("Avis", backref="utilisateur", lazy=True)

    # Convertit l'objet Utilisateur en dictionnaire (pour JSON)
    def to_dict(self):
        return {
            "iduser": self.iduser,
            "username": self.username,
            "emailuser": self.emailuser,
            "mdpuser": self.mdpuser,
            "admin": self.admin
        }

    # Récupère tous les utilisateurs sous forme de liste de dictionnaires
    @staticmethod
    def get_all_json():
        return [user.to_dict() for user in Utilisateur.query.all()]

    # Récupère un utilisateur par son id et le retourne sous forme de dictionnaire
    @staticmethod
    def get_by_id_json(iduser):
        user = Utilisateur.query.get_or_404(iduser)
        return user.to_dict()

    # Crée un nouvel utilisateur à partir d'un dictionnaire et le retourne sous forme de dictionnaire
    @staticmethod
    def create_from_json(data):
        user = Utilisateur(
            iduser=data["iduser"],
            username=data["username"],
            emailuser=data["emailuser"],
            mdpuser=data["mdpuser"],
            admin=(data.get("admin") == "on")  # <== case à cocher HTML
        )
        db.session.add(user)
        db.session.commit()
        return user.to_dict()

    # Met à jour un utilisateur existant à partir d'un dictionnaire et retourne le résultat sous forme de dictionnaire
    @staticmethod
    def update_from_json(iduser, data):
        user = Utilisateur.query.get_or_404(iduser)
        user.username = data.get("username", user.username)
        user.emailuser = data.get("emailuser", user.emailuser)
        user.mdpuser = data.get("mdpuser", user.mdpuser)
        user.admin = data.get("admin") == "on"  # ✅ conversion propre pour checkbox
        db.session.commit()
        return user.to_dict()

    # Supprime un utilisateur par son id et retourne un message de confirmation
    @staticmethod
    def delete_by_id(iduser):
        user = Utilisateur.query.get_or_404(iduser)
        db.session.delete(user)
        db.session.commit()
        return {"message": "Utilisateur supprimé"}


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

    # Convertit l'objet Etablissement en dictionnaire (pour JSON)
    def to_dict(self):
        return {
            "id": self.idetab,
            "nom": self.nometab,
            "adresse": self.adetab,
            "ville": self.villeetab,
            "cp": self.cpetab,
            "tel": self.teletab,
            "siteweb": self.sitewebetab,
            "idcat": self.idcat
        }

    # Récupère tous les établissements sous forme de liste de dictionnaires
    @staticmethod
    def get_all_json():
        return [e.to_dict() for e in Etablissement.query.all()]

    # Récupère un établissement par son id et le retourne sous forme de dictionnaire
    @staticmethod
    def get_by_id_json(idetab):
        e = Etablissement.query.get_or_404(idetab)
        return e.to_dict()

    # Crée un nouvel établissement à partir d'un dictionnaire et le retourne sous forme de dictionnaire
    @staticmethod
    def create_from_json(data):
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
        return etab.to_dict()

    # Met à jour un établissement existant à partir d'un dictionnaire et retourne le résultat sous forme de dictionnaire
    @staticmethod
    def update_from_json(idetab, data):
        etab = Etablissement.query.get_or_404(idetab)
        etab.nometab = data.get("nometab", etab.nometab)
        etab.adetab = data.get("adetab", etab.adetab)
        etab.villeetab = data.get("villeetab", etab.villeetab)
        etab.cpetab = data.get("cpetab", etab.cpetab)
        etab.teletab = data.get("teletab", etab.teletab)
        etab.sitewebetab = data.get("sitewebetab", etab.sitewebetab)
        etab.idcat = data.get("idcat", etab.idcat)
        db.session.commit()
        return etab.to_dict()

    # Supprime un établissement par son id et retourne un message de confirmation
    @staticmethod
    def delete_by_id(idetab):
        etab = Etablissement.query.get_or_404(idetab)
        db.session.delete(etab)
        db.session.commit()
        return {"message": "Etablissement supprimé"}


class Categorie(db.Model):
    idcat = db.Column(db.String(6), primary_key=True)
    nomcat = db.Column(db.String(30), nullable=False)

    etablissements = db.relationship("Possede", back_populates="categorie")

    # Convertit l'objet Categorie en dictionnaire (pour JSON)
    def to_dict(self):
        return {
            "idcat": self.idcat,
            "nomcat": self.nomcat
        }

    # Récupère toutes les catégories sous forme de liste de dictionnaires
    @staticmethod
    def get_all_json():
        return [cat.to_dict() for cat in Categorie.query.all()]

    # Récupère une catégorie par son id et la retourne sous forme de dictionnaire
    @staticmethod
    def get_by_id_json(idcat):
        cat = Categorie.query.get_or_404(idcat)
        return cat.to_dict()

    # Crée une nouvelle catégorie à partir d'un dictionnaire et la retourne sous forme de dictionnaire
    @staticmethod
    def create_from_json(data):
        cat = Categorie(
            idcat=data["idcat"],
            nomcat=data["nomcat"]
        )
        db.session.add(cat)
        db.session.commit()
        return cat.to_dict()

    # Met à jour une catégorie existante à partir d'un dictionnaire et retourne le résultat sous forme de dictionnaire
    @staticmethod
    def update_from_json(idcat, data):
        cat = Categorie.query.get_or_404(idcat)
        cat.nomcat = data.get("nomcat", cat.nomcat)
        db.session.commit()
        return cat.to_dict()

    # Supprime une catégorie par son id et retourne un message de confirmation
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

    iduser = db.Column(db.String(6), db.ForeignKey("utilisateur.iduser"), nullable=False)
    idetab = db.Column(db.String(6), db.ForeignKey("etablissement.idetab"), nullable=False)

    # Convertit l'objet Avis en dictionnaire (pour JSON)
    def to_dict(self):
        return {
            "idav": self.idav,
            "note": self.note,
            "commentaire": self.commentaire,
            "datecreation": self.datecreation.isoformat(),
            "iduser": self.iduser,
            "idetab": self.idetab
        }

    # Récupère tous les avis sous forme de liste de dictionnaires
    @staticmethod
    def get_all_json():
        return [avis.to_dict() for avis in Avis.query.all()]

    # Récupère un avis par son id et le retourne sous forme de dictionnaire
    @staticmethod
    def get_by_id_json(idav):
        avis = Avis.query.get_or_404(idav)
        return avis.to_dict()

    # Crée un nouvel avis à partir d'un dictionnaire et le retourne sous forme de dictionnaire
    @staticmethod
    def create_from_json(data):
        avis = Avis(
            idav=data["idav"],
            note=data["note"],
            commentaire=data["commentaire"],
            datecreation=data["datecreation"],
            iduser=data["iduser"],
            idetab=data["idetab"]
        )
        db.session.add(avis)
        db.session.commit()
        return avis.to_dict()

    # Met à jour un avis existant à partir d'un dictionnaire et retourne le résultat sous forme de dictionnaire
    @staticmethod
    def update_from_json(idav, data):
        avis = Avis.query.get_or_404(idav)
        avis.note = data.get("note", avis.note)
        avis.commentaire = data.get("commentaire", avis.commentaire)
        avis.datecreation = data.get("datecreation", avis.datecreation)
        avis.iduser = data.get("iduser", avis.iduser)
        avis.idetab = data.get("idetab", avis.idetab)
        db.session.commit()
        return avis.to_dict()

    # Supprime un avis par son id et retourne un message de confirmation
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

    # Convertit l'objet Possede en dictionnaire (pour JSON)
    def to_dict(self):
        return {
            "idcat": self.idcat,
            "idetab": self.idetab
        }

    # Récupère toutes les relations Possede sous forme de liste de dictionnaires
    @staticmethod
    def get_all_json():
        return [possede.to_dict() for possede in Possede.query.all()]

    # Récupère une relation Possede par idcat et idetab et la retourne sous forme de dictionnaire
    @staticmethod
    def get_by_id_json(idcat, idetab):
        possede = Possede.query.get_or_404((idcat, idetab))
        return possede.to_dict()

    # Crée une nouvelle relation Possede à partir d'un dictionnaire et la retourne sous forme de dictionnaire
    @staticmethod
    def create_from_json(data):
        possede = Possede(
            idcat=data["idcat"],
            idetab=data["idetab"]
        )
        db.session.add(possede)
        db.session.commit()
        return possede.to_dict()

    # Met à jour une relation Possede existante avec les données du formulaire
    @staticmethod
    def update_from_json(possede, data):
        possede.idcat = data["idcat"]
        possede.idetab = data["idetab"]
        db.session.commit()
        return possede.to_dict()
    
    # Supprime une relation Possede par idcat et idetab et retourne un message de confirmation
    @staticmethod
    def delete_by_id(idcat, idetab):
        possede = Possede.query.get_or_404((idcat, idetab))
        db.session.delete(possede)
        db.session.commit()
        return {"message": "Relation supprimée"}
