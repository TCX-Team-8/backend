
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

