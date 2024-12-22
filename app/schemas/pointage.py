from pydantic import BaseModel
from typing import Optional
from datetime import date, time, timedelta


class PointageBase(BaseModel):
    employe_id: Optional[int]
    date: date
    heure_entree: time
    heure_sortie: time
class PointageCreate(PointageBase):
    """
    Schema for creating a Pointage record.
    """
    pass


class PointageUpdate(BaseModel):
    """
    Schema for updating a Pointage record.
    """
    heure_entree: Optional[time]
    heure_sortie: Optional[time]
    
class AbsenceBase(BaseModel):
    employe_id: int
    justificatif: str


class RetardBase(BaseModel):
    pointage_id: int
    retard: timedelta
    justificatif: str