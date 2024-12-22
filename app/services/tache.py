from sqlmodel import Session, select
from app.models.tache import StatusTache, Tache, TacheAssignee
from app.schemas.tache import TacheBase, TacheAssigneeBase

class TacheService:
    @staticmethod
    def create_tache(session: Session, tache_data: TacheBase, assignation_data: TacheAssigneeBase):

        """
        Créer une tâche et l'assigner à un employé en une seule opération.
        """
        # Créer la tâche
        tache = Tache(**tache_data.model_dump())
        session.add(tache)
        session.commit()
        session.refresh(tache)

        # Lier l'assignation à la tâche créée
        assignation_data.tache_id = tache.id  # Assigner la tâche à un employé
        assignation = TacheAssignee(**assignation_data.model_dump())
        session.add(assignation)
        session.commit()

        # Retourner la tâche et l'assignation
        return {"tache": tache}
    
    @staticmethod
    def get_taches_by_id(session: Session, employe_id: int):
        """
        Récupérer toutes les tâches assignées à un employé donné.
        """
        try:
            # Requête pour récupérer les tâches liées à l'employé
            query = (
                select(Tache)
                .join(TacheAssignee, TacheAssignee.tache_id == Tache.id)
                .where(TacheAssignee.employe_id == employe_id)
            )
            result = session.exec(query).all()

            # Vérifier si des tâches existent
            if not result:
                return []

            return result
        except Exception as e:
            raise e
        
    @staticmethod
    def update_statut_tache(session: Session, employe_id: int, tache_id: int, nouveau_statut: StatusTache):
        """
        Permet à un employé de changer le statut d'une tâche assignée.
        """
        # Rechercher la tâche assignée
        tache_assignee = session.exec(
            select(TacheAssignee).where(
                TacheAssignee.employe_id == employe_id,
                TacheAssignee.tache_id == tache_id
            )
        ).first()


        if not tache_assignee:
            raise ValueError("Tâche non trouvée ou non assignée à cet employé.")

        # Modifier le statut
        tache_assignee.statut = nouveau_statut
        session.commit()
        session.refresh(tache_assignee)

        return tache_assignee


