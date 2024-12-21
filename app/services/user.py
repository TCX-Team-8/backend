from sqlmodel import Session, select
from ..models.user import Utilisateur

class UtilisateurService:
    @staticmethod
    def create_utilisateur(session: Session, utilisateur: Utilisateur) -> Utilisateur:
        """
        Create a new utilisateur and add it to the database.
        """
        session.add(utilisateur)
        session.commit()
        session.refresh(utilisateur)  # Refresh to get the ID and other defaults
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
