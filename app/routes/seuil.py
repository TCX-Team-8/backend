from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from ..services.seuil import SeuilService
from ..models.seuil import Seuil
from ..schemas.seuil import SeuilCreate
from ..database import get_session

seuil_router = APIRouter()

# Route to create a new Seuil
@seuil_router.post("/", response_model=Seuil)
def create_seuil(seuil: SeuilCreate, session: Session = Depends(get_session)):
    new_seuil = Seuil(**seuil.model_dump())
    created_seuil = SeuilService.create_seuil(session, new_seuil)
    return created_seuil

# Route to get all Seuil records
@seuil_router.get("/")
def get_all_seuils(session: Session = Depends(get_session)):
    all_seuils = SeuilService.get_all_seuils(session)
    return all_seuils

# Route to get a Seuil by ID
@seuil_router.get("/{seuil_id}", response_model=Seuil)
def get_seuil_by_id(seuil_id: int, session: Session = Depends(get_session)):
    try:
        seuil = SeuilService.get_seuil_by_id(session, seuil_id)
        return seuil
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# Route to update a Seuil
@seuil_router.put("/{seuil_id}", response_model=Seuil)
def update_seuil(seuil_id: int, seuil: SeuilCreate, session: Session = Depends(get_session)):
    updates = seuil.model_dump(exclude_unset=True)
    try:
        updated_seuil = SeuilService.update_seuil(session, seuil_id, updates)
        return updated_seuil
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# Route to delete a Seuil
@seuil_router.delete("/{seuil_id}")
def delete_seuil(seuil_id: int, session: Session = Depends(get_session)):
    try:
        SeuilService.delete_seuil(session, seuil_id)
        return {"message": "Seuil deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
