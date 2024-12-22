from datetime import date, timedelta
from typing import Optional
from sqlmodel import SQLModel, Field

class Seuil(SQLModel, table=True):
    __tablename__ = "seuils"  
    id: Optional[int] = Field(default=None, primary_key=True)
    seuil_retard: timedelta  
    seuil_absence: int       
    date_debut: date         
    date_fin: date           