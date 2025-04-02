#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: Utilisateur
#------------------------------------------------------------

CREATE TABLE Utilisateur(
        iduser    Varchar (6) NOT NULL ,
        username  Varchar (6) NOT NULL ,
        emailuser Varchar (90) NOT NULL ,
        mdpuser   Varchar (90) NOT NULL ,
        admin     Bool NOT NULL
	,CONSTRAINT Utilisateur_PK PRIMARY KEY (iduser)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Etablissement
#------------------------------------------------------------

CREATE TABLE Etablissement(
        idetab      Varchar (6) NOT NULL ,
        nometab     Varchar (30) NOT NULL ,
        adetab      Varchar (80) NOT NULL ,
        villeetab   Varchar (40) NOT NULL ,
        cpetab      Varchar (8) NOT NULL ,
        teletab     Varchar (15) NOT NULL ,
        sitewebetab Varchar (80) NOT NULL ,
        idcat       Varchar (6) NOT NULL
	,CONSTRAINT Etablissement_AK UNIQUE (idcat)
	,CONSTRAINT Etablissement_PK PRIMARY KEY (idetab)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Avis
#------------------------------------------------------------

CREATE TABLE Avis(
        idav                 Varchar (6) NOT NULL ,
        note                 Float NOT NULL ,
        commentaire          Varchar (200) NOT NULL ,
        datecreation         Date NOT NULL ,
        iduser               Varchar (6) NOT NULL ,
        idetab               Varchar (6) NOT NULL ,
        iduser_Utilisateur   Varchar (6) NOT NULL ,
        idetab_Etablissement Varchar (6) NOT NULL
	,CONSTRAINT Avis_AK UNIQUE (iduser,idetab)
	,CONSTRAINT Avis_PK PRIMARY KEY (idav)

	,CONSTRAINT Avis_Utilisateur_FK FOREIGN KEY (iduser_Utilisateur) REFERENCES Utilisateur(iduser)
	,CONSTRAINT Avis_Etablissement0_FK FOREIGN KEY (idetab_Etablissement) REFERENCES Etablissement(idetab)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Categorie
#------------------------------------------------------------

CREATE TABLE Categorie(
        idcat  Varchar (6) NOT NULL ,
        nomcat Varchar (30) NOT NULL
	,CONSTRAINT Categorie_PK PRIMARY KEY (idcat)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: possede
#------------------------------------------------------------

CREATE TABLE possede(
        idcat  Varchar (6) NOT NULL ,
        idetab Varchar (6) NOT NULL
	,CONSTRAINT possede_PK PRIMARY KEY (idcat,idetab)

	,CONSTRAINT possede_Categorie_FK FOREIGN KEY (idcat) REFERENCES Categorie(idcat)
	,CONSTRAINT possede_Etablissement0_FK FOREIGN KEY (idetab) REFERENCES Etablissement(idetab)
)ENGINE=InnoDB;

