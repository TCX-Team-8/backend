from datetime import time, timedelta, date
from sqlmodel import Session, select
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
    def handle_retard_and_absence(session: Session, pointage: Pointage):
        """
        Handle Retard and Absence logic:
        - Create a Retard if heure_sortie is before 16:30 
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
