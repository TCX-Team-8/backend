from sqlalchemy import select
from sqlmodel import Session
from ..models.user import Utilisateur, RH, Admin, Employe

class UtilisateurService:
    @staticmethod
    def create_utilisateur(session: Session, utilisateur: Utilisateur, departement_id: int) -> Utilisateur:
        """
        Create a new utilisateur, assign the role based on departement_id, and add it to the database.
        """
        session.add(utilisateur)
        session.commit()  
        session.refresh(utilisateur)  

        if departement_id == 0: # RH
            role = RH(id_utilisateur=utilisateur.id)
        elif departement_id == 1:  # Admin
            role = Admin(id_utilisateur=utilisateur.id)
        else:  # Employe
            role = Employe(id_utilisateur=utilisateur.id)
       
        session.add(role)
        session.commit()
        return utilisateur

    @staticmethod
    def get_utilisateur_by_id(session: Session, utilisateur_id: int) -> Utilisateur:
        """
        Retrieve a utilisateur by ID.
        """
        return session.get(Utilisateur, utilisateur_id)

    @staticmethod
    def get_all_utilisateurs(session: Session):
        """
        Retrieve all utilisateurs.
        """
        statement = select(Utilisateur)
        return session.exec(statement).all()

    @staticmethod
    def update_utilisateur(session: Session, utilisateur_id: int, updates: dict) -> Utilisateur:
        """
        Update a utilisateur by ID with the provided updates dictionary.
        """
        utilisateur = session.get(Utilisateur, utilisateur_id)
        if not utilisateur:
            raise ValueError(f"Utilisateur with ID {utilisateur_id} not found")

        for key, value in updates.items():
            if hasattr(utilisateur, key):
                setattr(utilisateur, key, value)

        session.add(utilisateur)
        session.commit()
        session.refresh(utilisateur)
        return utilisateur

    @staticmethod
    def delete_utilisateur(session: Session, utilisateur_id: int) -> None:
        """
        Delete a utilisateur by ID.
        """
        utilisateur = session.get(Utilisateur, utilisateur_id)
        if not utilisateur:
            raise ValueError(f"Utilisateur with ID {utilisateur_id} not found")

        session.delete(utilisateur)
        session.commit()