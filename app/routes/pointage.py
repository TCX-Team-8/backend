from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from datetime import date
from ..services.pointage import PointageService
from ..models.pointage import Pointage
from ..schemas.pointage import PointageCreate, PointageUpdate
from ..database import get_session

pointage_router = APIRouter()


@pointage_router.post("/", response_model=Pointage)
def create_pointage(pointage: PointageCreate, session: Session = Depends(get_session)):
    """
    Create a new pointage record.
    """
    try:
        # Create a new pointage entry, ensuring employe_id is set correctly
        new_pointage = Pointage(**pointage.dict())
        created_pointage = PointageService.create_pointage(session, new_pointage)
        return created_pointage
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@pointage_router.put("/", response_model=Pointage)
def update_pointage(
    employe_id: int, 
    date_to_check: date, 
    pointage: PointageUpdate, 
    session: Session = Depends(get_session)
):
    """
    Update an existing pointage record by employe_id and date.
    Handles Retard and Absence logic when heure_entree or heure_sortie are updated.
    """
    try:
        # Create a dictionary of the updates and pass them to the service for processing
        updates = pointage.dict(exclude_unset=True)
        updated_pointage = PointageService.update_pointage(session, employe_id, date_to_check, updates)
        return updated_pointage
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@pointage_router.get("/", response_model=list[Pointage])
def get_all_pointages(session: Session = Depends(get_session)):
    """
    Retrieve all pointage records.
    """
    return PointageService.get_all_pointages(session)


@pointage_router.get("/{pointage_id}", response_model=Pointage)
def get_pointage_by_id(pointage_id: int, session: Session = Depends(get_session)):
    """
    Retrieve a single pointage record by ID.
    """
    pointage = PointageService.get_pointage_by_id(session, pointage_id)
    if not pointage:
        raise HTTPException(status_code=404, detail="Pointage not found")
    return pointage


@pointage_router.delete("/{pointage_id}")
def delete_pointage(pointage_id: int, session: Session = Depends(get_session)):
    """
    Delete a pointage record by ID.
    """
    try:
        PointageService.delete_pointage(session, pointage_id)
        return {"message": "Pointage deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@pointage_router.get("/absences/{date_to_check}", response_model=dict)
def generate_absences(date_to_check: date, session: Session = Depends(get_session)):
    """
    Generate and retrieve absences for a given date.
    """
    try:
        # Call the service method to generate absences
        PointageService.generate_absences(session, date_to_check)
        return {"message": f"Absences generated for {date_to_check}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))