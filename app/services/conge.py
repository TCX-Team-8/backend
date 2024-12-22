from sqlmodel import Session, select
from ..models.conge import Conge

class CongeService:
    @staticmethod
    def create_conge(session: Session, conge: Conge) -> Conge:
        """
        Create a new Conge and add it to the database.
        """
        session.add(conge)
        session.commit()  
        session.refresh(conge)  
        return conge

    @staticmethod
    def get_all_conge(session: Session):
        """
        Retrieve all Conge records from the database.
        """
        statement = select(Conge)
        return session.exec(statement).all()  

    @staticmethod
    def get_conge_by_id(session: Session, conge_id: int) -> Conge:
        """
        Retrieve a specific Conge by its ID.
        """
        conge = session.get(Conge, conge_id)
        if not conge:
            raise ValueError(f"Conge with ID {conge_id} not found")
        return conge

    @staticmethod
    def update_conge(session: Session, conge_id: int, updates: dict) -> Conge:
        """
        Update an existing Conge record by its ID.
        """
        conge = session.get(Conge, conge_id)
        if not conge:
            raise ValueError(f"Conge with ID {conge_id} not found")

        for key, value in updates.items():
            if hasattr(conge, key):
                setattr(conge, key, value)

        session.add(conge)  
        session.commit() 
        session.refresh(conge)  
        return conge

    @staticmethod
    def delete_conge(session: Session, conge_id: int) -> None:
        """
        Delete a specific Conge record by its ID.
        """
        conge = session.get(Conge, conge_id)
        if not conge:
            raise ValueError(f"Conge with ID {conge_id} not found")

        session.delete(conge)  
        session.commit()  