from pydantic import BaseModel
from typing import Optional
from datetime import date, time, timedelta


class PointageBase(BaseModel):
    employe_id: Optional[int]
    date: date
    heure_entree: time
    heure_sortie: time

class AbsenceBase(BaseModel):
    pointage_id: int
    justificatif: str


class RetardBase(BaseModel):
    pointage_id: int
    retard: timedelta
    justificatif: str




# from datetime import date, time, timedelta
# from typing import Optional
# from sqlmodel import Field, SQLModel

# class Pointage(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     employe_id: Optional[int] = Field(default=None, foreign_key="employe.id_utilisateur")
#     date: date
#     heure_entree: time
#     heure_sortie: time
    
# class Absence(SQLModel, table=True):
#     pointage_id: Optional[int] = Field(default=None, foreign_key="pointage.id", primary_key=True)
#     justificatif: str

# class Retard(SQLModel, table=True):
#     pointage_id: Optional[int] = Field(default=None, foreign_key="pointage.id", primary_key=True)
#     retard: timedelta  
#     justificatif: str