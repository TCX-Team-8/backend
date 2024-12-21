
from pydantic import BaseModel
from typing import Optional
from enum import Enum

# Enum for notification status
class StatusNotification(str, Enum):
    ENVOYEE = "envoyee"
    NON_ENVOYEE = "non_envoyee"

class NotificationBase(BaseModel):
    employe_id: Optional[int]
    rh_id: Optional[int]
    statut: StatusNotification = StatusNotification.NON_ENVOYEE

class RappelBase(BaseModel):
    notification_id: int
    employe_id: int
    tache_id: int

class AvertissementAbsenceBase(BaseModel):
    notification_id: int
    absence_id: int

class AvertissementRetardBase(BaseModel):
    notification_id: int
    retard_id: int



# from enum import Enum
# from typing import Optional
# from sqlmodel import Field, SQLModel

# class StatusNotification(str, Enum):
#     ENVOYEE = "envoyee"
#     NON_ENVOYEE = "non_envoyee"


# class Notification(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     employe_id: Optional[int] = Field(default=None, foreign_key="employe.id_utilisateur")
#     rh_id: Optional[int] = Field(default=None, foreign_key="rh.id_utilisateur")
#     statut: StatusNotification = Field(default=StatusNotification.NON_ENVOYEE)

# # class NotificationTacheAssignee(SQLModel, table=True):
# #     notification_id: Optional[int] = Field(default=None, foreign_key="notification.id", primary_key=True)
# #     employe_id: Optional[int] = Field(default=None, foreign_key="tacheassignee.employe_id")
# #     tache_id: Optional[int] = Field(default=None, foreign_key="tacheassignee.tache_id")

# class Rappel(SQLModel, table=True):
#     notification_id: Optional[int] = Field(default=None, foreign_key="notification.id", primary_key=True)
#     employe_id: Optional[int] = Field(default=None, foreign_key="tacheassignee.employe_id")
#     tache_id: Optional[int] = Field(default=None, foreign_key="tacheassignee.tache_id")


# class AvertissementAbsence(SQLModel, table=True):
#     notification_id: Optional[int] = Field(default=None, foreign_key="notification.id", primary_key=True)
#     absence_id: Optional[int] = Field(default=None, foreign_key="absence.pointage_id")

# class AvertissementRetard(SQLModel, table=True):
#     notification_id: Optional[int] = Field(default=None, foreign_key="notification.id", primary_key=True)
#     retard_id: Optional[int] = Field(default=None, foreign_key="retard.pointage_id")