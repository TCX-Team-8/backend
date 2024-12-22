from pydantic import BaseModel
from datetime import date, timedelta

class SeuilBase(BaseModel):
    seuil_retard: timedelta
    seuil_absence: int
    date_debut: date
    date_fin: date
    
class SeuilCreate(BaseModel):
    seuil_retard: timedelta
    seuil_absence: int
    date_debut: date
    date_fin: date
    class Config:
        orm_mode = True  
