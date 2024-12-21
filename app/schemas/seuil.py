from pydantic import BaseModel
from datetime import date, timedelta

class SeuilBase(BaseModel):
    seuil_retard: timedelta
    seuil_absence: int
    date_debut: date
    date_fin: date


# from datetime import date, timedelta
# from typing import Optional
# from sqlmodel import Field, SQLModel

# class Seuil(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     seuil_retard: timedelta
#     seuil_absence : int
#     date_debut: date
#     date_fin: date
    