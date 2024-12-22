from sqlmodel import Session, select
from app.models import pointage
from app.models.notification import Notification, AvertissementAbsence, AvertissementRetard, StatusNotification
from app.models.seuil import Seuil
from app.models.pointage import Absence, Pointage, Retard
from datetime import datetime

class NotificationService:
    @staticmethod
    def create_notification(session: Session):
        """
        Envoie un avertissement pour les retards dépassant le seuil.
        Met à jour le statut de la notification pour éviter les spams.
        """

        seuil_retard = session.exec(
            select(Seuil).where(
                Seuil.date_debut <= datetime.now(),
                Seuil.date_fin >= datetime.now()
            )
        ).first()

        if not seuil_retard:
            return {"message": "Aucun seuil d'absence actif trouvé."}

        # Sélectionner les retards dont la durée dépasse le seuil
        retards = session.exec(
            select(Retard.pointage_id, Retard.retard)
            .where(Retard.retard >= seuil_retard.seuil_retard)
        ).all()

        for pointage_id, retard in retards:
            # Récupérer l'employé associé au pointage
            pointage = session.get(Pointage, pointage_id)
            if pointage is None:
                continue  # Si le pointage n'existe pas, on passe au suivant


            employe_id = pointage.employe_id  # Récupérer l'employe_id à partir du pointage

            # Créer une nouvelle notification
            notification = Notification(
                employe_id=employe_id,
                statut=StatusNotification.NON_ENVOYEE  
            )

            # Ajouter la notification dans la session
            session.add(notification)
            session.commit()

        return {"message": f"Vous avez dépassé le seuil de {seuil_retard.seuil_retard} minutes de retard, faites plus attention !"}
    
    @staticmethod
    def create_avertissement_retard(session: Session, notification_id: int, pointage_id: int):
        """
        Envoie une notification (change le statut à 'ENVOYEE').
        """
        notification = session.get(Notification, notification_id)
        if not notification:
            return {"message": "Notification non trouvée."}

        # Mettre à jour le statut de la notification
        notification.statut = StatusNotification.ENVOYEE
        session.add(notification)
        session.commit()

        # Créer un avertissement pour le retard
        avertissement = AvertissementRetard(
            notification_id=notification.id,
            retard_id=pointage_id
        )
        session.add(avertissement)
        session.commit()

        return {"message": "Avertissement envoyée avec succès."}
    
    @staticmethod
    def afficher_notifications(session: Session):
        """
        Récupère les notifications en attente (non envoyées).
        """
        notifications = session.exec(
            select(Notification).where(Notification.statut == StatusNotification.NON_ENVOYEE)
        ).all()

        if not notifications:
            return {"message": "Aucune notification en attente."}

        return {"notifications": notifications}