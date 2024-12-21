from sqlmodel import Session, select
from ..models.seuil import Seuil

class SeuilService:
    @staticmethod
    def create_seuil(session: Session, seuil: Seuil) -> Seuil:
        """
        Create a new Seuil and add it to the database.
        """
        session.add(seuil)
        session.commit()  
        session.refresh(seuil)  
        return seuil

    @staticmethod
    def get_all_seuils(session: Session):
        """
        Retrieve all Seuil records from the database.
        """
        statement = select(Seuil)
        return session.exec(statement).all()  

    @staticmethod
    def get_seuil_by_id(session: Session, seuil_id: int) -> Seuil:
        """
        Retrieve a specific Seuil by its ID.
        """
        seuil = session.get(Seuil, seuil_id)
        if not seuil:
            raise ValueError(f"Seuil with ID {seuil_id} not found")
        return seuil

    @staticmethod
    def update_seuil(session: Session, seuil_id: int, updates: dict) -> Seuil:
        """
        Update an existing Seuil record by its ID.
        """
        seuil = session.get(Seuil, seuil_id)
        if not seuil:
            raise ValueError(f"Seuil with ID {seuil_id} not found")

        for key, value in updates.items():
            if hasattr(seuil, key):
                setattr(seuil, key, value)

        session.add(seuil)  
        session.commit()  
        session.refresh(seuil)  
        return seuil

    @staticmethod
    def delete_seuil(session: Session, seuil_id: int) -> None:
        """
        Delete a specific Seuil record by its ID.
        """
        seuil = session.get(Seuil, seuil_id)
        if not seuil:
            raise ValueError(f"Seuil with ID {seuil_id} not found")

        session.delete(seuil)  
        session.commit()  
