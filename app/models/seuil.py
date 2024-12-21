from datetime import date, timedelta
from typing import Optional
from sqlmodel import SQLModel, Field

class Seuil(SQLModel, table=True):
    __tablename__ = "seuils"  # Specify the table name
    id: Optional[int] = Field(default=None, primary_key=True)
    seuil_retard: timedelta  # Threshold for delay
    seuil_absence: int       # Threshold for absence
    date_debut: date         # Start date
    date_fin: date           # End date
