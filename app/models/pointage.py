from datetime import date, time, timedelta
from typing import Optional
from sqlmodel import SQLModel, Field

class Pointage(SQLModel, table=True):
    __tablename__ = "pointages"  # Specify table name
    id: Optional[int] = Field(default=None, primary_key=True)
    employe_id: Optional[int] = Field(default=None, foreign_key="employe.id_utilisateur")
    date: date
    heure_entree: time
    heure_sortie: time


class Absence(SQLModel, table=True):
    __tablename__ = "absences"  # Specify table name
    pointage_id: Optional[int] = Field(default=None, foreign_key="pointages.id", primary_key=True)
    justificatif: str


class Retard(SQLModel, table=True):
    __tablename__ = "retards"  # Specify table name
    pointage_id: Optional[int] = Field(default=None, foreign_key="pointages.id", primary_key=True)
    retard: timedelta  
    justificatif: str
