
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from ..services.conge import CongeService
from ..models.conge import Conge
from ..schemas.conge import CongeCreate
from ..database import get_session

conge_router = APIRouter()

# Route to create a new user
@conge_router.post("/", response_model=Conge)
def create_conge(conge: CongeCreate, session: Session = Depends(get_session)):
    new_conge = Conge(**conge.model_dump())
    created_conge = CongeService.create_conge(session, new_conge)
    return created_conge

# Route to get all users
@conge_router.get("/")
def get_all_conge(session: Session = Depends(get_session)):
    all_users = CongeService.get_all_conge(session)
    return all_users

# Route to update a user
@conge_router.put("/{conge_id}", response_model=Conge)
def update_conge(conge_id: int, conge: CongeCreate, session: Session = Depends(get_session)):
    updates = conge.model_dump(exclude_unset=True)
    updated_conge = CongeService.update_conge(session, conge_id, updates)
    if not updated_conge:
        raise HTTPException(status_code=404, detail="Conge not found")
    return updated_conge

# Route to delete a user
@conge_router.delete("/{conge_id}")
def delete_conge(conge_id: int, session: Session = Depends(get_session)):
    CongeService.delete_conge(session, conge_id)
    return {"message": "Conge deleted"}
