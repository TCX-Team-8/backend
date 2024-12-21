from datetime import date
from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field

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

# Conge model
class Conge(SQLModel, table=True):
    __tablename__ = "conges"  # Specify table name
    id: Optional[int] = Field(default=None, primary_key=True)
    employe_id: Optional[int] = Field(default=None, foreign_key="employe.id_utilisateur")
    type: TypeConge
    date_debut: date
    date_fin: date
    statut: StatutConge
    motif: str
