from datetime import date
from enum import Enum
from typing import Optional
from sqlmodel import Field, SQLModel


# Enum for task priority
class PrioriteTache(str, Enum):
    ELEVEE = "elevee"
    MOYENNE = "moyenne"
    FAIBLE = "faible"


# Enum for task status
class StatusTache(str, Enum):
    TERMINEE = "terminee"
    NON_TERMINEE = "non_terminee"


# Tache model
class Tache(SQLModel, table=True):
    __tablename__ = "taches"  
    id: Optional[int] = Field(default=None, primary_key=True)
    intitule: str
    description: str
    priorite: PrioriteTache
    deadline: date


# TacheAssignee model (assigning tasks to employees)
class TacheAssignee(SQLModel, table=True):
    __tablename__ = "taches_assignees"  # Specify the table name
    employe_id: Optional[int] = Field(default=None, foreign_key="employe.id_utilisateur", primary_key=True)
    tache_id: Optional[int] = Field(default=None, foreign_key="taches.id", primary_key=True)
    statut: StatusTache = Field(default=StatusTache.NON_TERMINEE)