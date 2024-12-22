from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.services.notification import NotificationService
from app.models.notification import StatusNotification
from app.database import get_session  # Assurez-vous d'avoir une fonction pour obtenir la session

notification_router = APIRouter()

# Route pour créer des avertissements de retard
@notification_router.post("/create_avertissement_retard")
async def create_notification(session: Session = Depends(get_session)):
    try:
        result = NotificationService.create_notification(session)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route pour afficher toutes les notifications non envoyées
@notification_router.get("/afficher_notifications")
async def afficher_notifications(session: Session = Depends(get_session)):
    try:
        result = NotificationService.afficher_notifications(session)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route pour envoyer une notification spécifique (en mettre à jour le statut à 'ENVOYEE')
@notification_router.post("/envoyer_notification/{notification_id}")
async def envoyer_notification(notification_id: int, session: Session = Depends(get_session)):
    try:
        result = NotificationService.create_avertissement_retard(session, notification_id, pointage_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
