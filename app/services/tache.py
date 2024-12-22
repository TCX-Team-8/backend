from datetime import date
from typing import List, Optional
from sqlmodel import Session, select
from ..models.tache import Tache, TacheAssignee, StatusTache
from sqlalchemy.orm import joinedload

class TacheService:

    @staticmethod
    def create_and_assign_tache(session: Session, tache: Tache, employe_id: int) -> Tache:
        """
        Create a new task in the database and assign it to an employee.
        """
        # Step 1: Create the task
        session.add(tache)
        session.commit()
        session.refresh(tache)

        # Step 2: Assign the task to the employee
        tache_assignee = TacheAssignee(employe_id=employe_id, tache_id=tache.id)
        session.add(tache_assignee)
        session.commit()
        session.refresh(tache_assignee)

        return tache

    @staticmethod
    def get_tache_by_id(session: Session, tache_id: int) -> Optional[Tache]:
        """
        Get a task by its ID.
        """
        return session.get(Tache, tache_id)

    @staticmethod
    def get_all_taches(session: Session) -> List[Tache]:
        """
        Retrieve all tasks.
        """
        return session.exec(select(Tache)).all()

    @staticmethod
    def update_tache(session: Session, tache_id: int, updates: dict) -> Optional[Tache]:
        """
        Update a task by ID with the provided updates dictionary.
        """
        tache = session.get(Tache, tache_id)
        if not tache:
            return None

        for key, value in updates.items():
            if hasattr(tache, key):
                setattr(tache, key, value)

        session.add(tache)
        session.commit()
        session.refresh(tache)
        return tache

    @staticmethod
    def delete_tache(session: Session, tache_id: int) -> bool:
        """
        Delete a task by ID.
        """
        tache = session.get(Tache, tache_id)
        if not tache:
            return False

        session.delete(tache)
        session.commit()
        return True

    @staticmethod
    def assign_tache_to_employe(session: Session, employe_id: int, tache_id: int) -> TacheAssignee:
        """
        Assign a task to an employee (this is now redundant, as the assignment is done in `create_and_assign_tache`).
        """
        tache_assignee = TacheAssignee(employe_id=employe_id, tache_id=tache_id)
        session.add(tache_assignee)
        session.commit()
        session.refresh(tache_assignee)
        return tache_assignee

    @staticmethod
    def get_assigned_tasks(session: Session, employe_id: int) -> List[Tache]:
        """
        Get all tasks assigned to an employee.
        """
        statement = select(Tache).join(TacheAssignee).where(TacheAssignee.employe_id == employe_id)
        return session.exec(statement).all()

    @staticmethod
    def update_task_status(session: Session, tache_id: int, status: StatusTache) -> Optional[TacheAssignee]:
        """
        Update the status of a task assigned to an employee.
        """
        statement = select(TacheAssignee).where(TacheAssignee.tache_id == tache_id)
        tache_assignee = session.exec(statement).first()
        
        if not tache_assignee:
            return None

        tache_assignee.statut = status
        session.commit()
        session.refresh(tache_assignee)
        return tache_assignee
