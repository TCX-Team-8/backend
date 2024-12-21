from sqlalchemy import create_engine
from sqlmodel import SQLModel, Field
from datetime import date
from typing import Optional

class Utilisateur(SQLModel, table=True):
    __tablename__ = "utilisateur"
    id: Optional[int] = Field(default=None, primary_key=True)
    nom: str
    prenom: str
    email: str
    tel: str
    tel_urgence: str
    lien_urgence: str
    nss: str
    adresse: str
    date_naissance: date
    departement_id: Optional[int] = Field(foreign_key="departement.id")
    photo: str
    mot_de_passe: str
    matricule: str

class Departement(SQLModel, table=True):
    __tablename__ = "departement"
    id: Optional[int] = Field(default=None, primary_key=True)
    intitule: str

class RH(SQLModel, table=True):
    __tablename__ = "rh"
    id_utilisateur: Optional[int] = Field(default=None, foreign_key="utilisateur.id", primary_key=True)

class Admin(SQLModel, table=True):
    __tablename__ = "admin"
    id_utilisateur: Optional[int] = Field(default=None, foreign_key="utilisateur.id", primary_key=True)

class Employe(SQLModel, table=True):
    __tablename__ = "employe"
    id_utilisateur: Optional[int] = Field(default=None, foreign_key="utilisateur.id", primary_key=True)



# Database URL (replace with your actual database URL)
DATABASE_URL = "sqlite:///database.db"  # Example using SQLite; adjust for other DBs

# Create an engine that connects to the database
engine = create_engine(DATABASE_URL)

# Create all the tables defined by the models
SQLModel.metadata.create_all(engine)

print("Database and tables created successfully.")