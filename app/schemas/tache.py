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





# from datetime import date
# from enum import Enum
# from typing import Optional
# from sqlmodel import Field, SQLModel

# class PrioriteTache(str, Enum):
#     ELEVEE = "elevee"
#     MOYENNE = "moyenne"
#     FAIBLE = "faible"
    
# class StatusTache(str, Enum):
#     TERMINEE = "terminee"
#     NON_TERMINEE = "non_terminee"

    
# class Tache(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     intitule: str
#     description: str
#     priorite: PrioriteTache
#     deadline: date

# class TacheAssignee(SQLModel, table=True):
#     employe_id: Optional[int] = Field(default=None, foreign_key="employe.id_utilisateur", primary_key=True)
#     tache_id: Optional[int] = Field(default=None, foreign_key="tache.id", primary_key=True)
#     statut: StatusTache = Field(default=StatusTache.NON_TERMINEE)



