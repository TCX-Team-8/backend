from datetime import date
from typing import Optional
from pydantic import BaseModel
from sqlmodel import Field, SQLModel

class Utilisateur(SQLModel):
    nom: str
    prenom: str
    email: str
    tel: str
    tel_urgence: str
    lien_urgence: str
    nss: str
    adresse: str
    date_naissance: date
    departement_id: int
    photo: str
    mot_de_passe: str
    matricule: str
class UtilisateurCreate(BaseModel):
    nom: str
    prenom: str
    email: str
    tel: str
    tel_urgence: str
    lien_urgence: str
    nss: str
    adresse: str
    date_naissance: date
    departement_id: int
    photo: str
    mot_de_passe: str
    matricule: str

    class Config:
        orm_mode = True  # This allows conversion from SQLModel to Pydantic model
        
class Departement(SQLModel):
    intitule: str

class RH(BaseModel):
    id_utilisateur: int

class Admin(BaseModel):
    id_utilisateur: int

class Employe(BaseModel):
    id_utilisateur: int
