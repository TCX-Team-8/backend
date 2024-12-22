from datetime import datetime, time, timedelta, date
from sqlmodel import Session, select

from app.models.notification import AvertissementRetard, Notification, StatusNotification
from app.models.seuil import Seuil
from ..models.pointage import Pointage, Absence, Retard
from ..models.user import Employe 


class PointageService:
    @staticmethod
    def create_pointage(session: Session, pointage: Pointage) -> Pointage:
        """
        Create a new Pointage record and add it to the database.
        """
        session.add(pointage)
        session.commit()
        session.refresh(pointage)
        return pointage

    @staticmethod
    def update_pointage(session: Session, employe_id: int, date_to_check: date, updates: dict) -> Pointage:
        """
        Update a Pointage record and handle business logic for Retard and Absence based on employe_id and date.
        """
        pointage = session.exec(
            select(Pointage).where(Pointage.employe_id == employe_id, Pointage.date == date_to_check)
        ).first()
        if not pointage:
            raise ValueError(f"Pointage for Employe ID {employe_id} on {date_to_check} not found")

        # Apply updates
        for key, value in updates.items():
            if hasattr(pointage, key):
                setattr(pointage, key, value)

        session.add(pointage)
        session.commit()

        if 'heure_sortie' in updates or 'heure_entree' in updates:
            PointageService.handle_retard_and_absence(session, pointage)

        session.refresh(pointage)
        return pointage

    @staticmethod
    def handle_retard_and_absence(session: Session, pointage: Pointage , ):
        """
        Handle Retard and Absence logic:
        - Create a Retard if heure_sortie is before 16:30 or heure_entree is after 08:30.
        - Create Absence records for employees who have no pointage for the given date.
        """
        expected_entree = time(8, 30)
        
        # Handle Retard
        if pointage.heure_entree and pointage.heure_sortie:
            retard_duration = timedelta()
            if pointage.heure_entree > expected_entree:
                retard_duration += timedelta(
                    hours=pointage.heure_entree.hour - expected_entree.hour,
                    minutes=pointage.heure_entree.minute - expected_entree.minute
                )
            
            if retard_duration > timedelta(0):  # If there is a delay
                existing_retard = session.exec(
                    select(Retard).where(Retard.pointage_id == pointage.id)
                ).first()

                if existing_retard:
                    existing_retard.retard = retard_duration
                    session.add(existing_retard)
                else:
                    new_retard = Retard(
                        pointage_id=pointage.id,
                        retard=retard_duration,
                        justificatif="Pas disponible"
                    )
                    session.add(new_retard)

        
        date_to_check = pointage.date
        all_employees = session.exec(select(Employe.id_utilisateur)).all()

        
        employees_with_pointage = session.exec(
            select(Pointage.employe_id).where(Pointage.date == date_to_check)
        ).all()

        absent_employees = set(all_employees) - set(employees_with_pointage)

        for employe_id in absent_employees:
            
            existing_absence = session.exec(
                select(Absence).where(Absence.employe_id == employe_id, Absence.justificatif == "Absent without pointage")
            ).first()

            if not existing_absence:
                new_absence = Absence(
                    employe_id=employe_id,  
                    justificatif="Pas disponible"  
                )
                session.add(new_absence)

        session.commit()

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

            # Créer un avertissement pour le retard
            avertissement = AvertissementRetard(
                notification_id=notification.id,
                retard_id=pointage_id
            )
            session.add(avertissement)
            session.commit()