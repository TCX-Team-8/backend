# main.py
from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlmodel import Session, create_engine, select
from app.database import get_session
from app.models.tache import StatusTache, Tache, TacheAssignee
from app.schemas.tache import TacheAssigneeBase, TacheBase
from app.services.tache import TacheService
from sqlalchemy.exc import SQLAlchemyError

# Initialiser FastAPI
tache_router = APIRouter()

# Route pour créer une tâche et l'assigner
@tache_router.post("/", response_model=dict)
def create_tache_view(
    tache_data: TacheBase, assignation_data: TacheAssigneeBase, session: Session = Depends(get_session)
):
    try:
        # Appel au contrôleur pour créer et assigner la tâche
        result = TacheService.creer_et_assigner_tache(session, tache_data, assignation_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@tache_router.get("/employes/{employe_id}/taches", response_model=list[TacheBase], tags=["taches"])
def get_taches_by_id_view(employe_id: int, session: Session = Depends(get_session)):
    try:
        result = TacheService.afficher_taches_employe(session, employe_id)
        if not result:
            raise HTTPException(status_code=404, detail="Aucune tâche trouvée pour cet employé.")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@tache_router.patch("/employes/{employe_id}/taches/{tache_id}/statut", response_model=dict, tags=["taches"])
def update_statut_tache_view(
    employe_id: int, tache_id: int, nouveau_statut: StatusTache, session: Session = Depends(get_session)
):
    """
    Permet à un employé de changer le statut d'une tâche qui lui est assignée.
    """
    try:
        tache_assignee = TacheService.modifier_statut_tache(session, employe_id, tache_id, nouveau_statut)
        return {"message": "Statut mis à jour avec succès.", "tache_assignee": tache_assignee}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
