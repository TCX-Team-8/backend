from pydantic import BaseModel
from datetime import date
from enum import Enum
from typing import Optional

# Enum for leave status
class StatutConge(str, Enum):
    EN_ATTENTE = "en_attente"
    APPROUVE = "approuve"
    REFUSE = "refuse"
    ANNULE = "annule"

# Enum for leave type
class TypeConge(str, Enum):
    MALADIE = "maladie"
    RTT = "rtt"
    PERSONNEL = "personnel"


# Base schema for Conge
class CongeBase(BaseModel):
    employe_id: Optional[int]
    type: TypeConge
    date_debut: date
    date_fin: date
    statut: StatutConge
    motif: str
    
class CongeCreate(BaseModel):
    employe_id: Optional[int]
    type: TypeConge
    date_debut: date
    date_fin: date
    statut: StatutConge
    motif: str
    class Config:
        orm_mode = True  