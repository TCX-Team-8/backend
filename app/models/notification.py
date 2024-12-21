from enum import Enum
from typing import Optional
from sqlalchemy import ForeignKeyConstraint
from sqlmodel import SQLModel, Field


# Enum for notification status
class StatusNotification(str, Enum):
    ENVOYEE = "envoyee"
    NON_ENVOYEE = "non_envoyee"


# Notification model
class Notification(SQLModel, table=True):
    __tablename__ = "notifications"  # Specify table name
    id: Optional[int] = Field(default=None, primary_key=True)
    employe_id: Optional[int] = Field(default=None, foreign_key="employe.id_utilisateur")
    rh_id: Optional[int] = Field(default=None, foreign_key="rh.id_utilisateur")
    statut: StatusNotification = Field(default=StatusNotification.NON_ENVOYEE)


# Rappel model

class Rappel(SQLModel, table=True):
    __tablename__ = "rappels"
    notification_id: Optional[int] = Field(default=None, foreign_key="notifications.id", primary_key=True)
    employe_id: Optional[int] = Field(default=None)  # Kept for reference
    tache_id: Optional[int] = Field(default=None)  # Kept for reference
    __table_args__ = (
        ForeignKeyConstraint(["employe_id", "tache_id"], ["taches_assignees.employe_id", "taches_assignees.tache_id"]),
    )


# AvertissementAbsence model
class AvertissementAbsence(SQLModel, table=True):
    __tablename__ = "avertissements_absence"  # Specify table name
    notification_id: Optional[int] = Field(default=None, foreign_key="notifications.id", primary_key=True)
    absence_id: Optional[int] = Field(default=None, foreign_key="absences.id")


# AvertissementRetard model
class AvertissementRetard(SQLModel, table=True):
    __tablename__ = "avertissements_retard"  # Specify table name
    notification_id: Optional[int] = Field(default=None, foreign_key="notifications.id", primary_key=True)
    retard_id: Optional[int] = Field(default=None, foreign_key="retards.pointage_id")
