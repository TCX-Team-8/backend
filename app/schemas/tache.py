from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum

# Enum for task priority
class PrioriteTache(str, Enum):
    ELEVEE = "elevee"
    MOYENNE = "moyenne"
    FAIBLE = "faible"


# Enum for task status
class StatusTache(str, Enum):
    TERMINEE = "terminee"
    NON_TERMINEE = "non_terminee"

class TacheBase(BaseModel):
    intitule: str
    description: str
    priorite: PrioriteTache
    deadline: date

class TacheAssigneeBase(BaseModel):
    employe_id: int
    tache_id: int
    statut: StatusTache = StatusTache.NON_TERMINEE
