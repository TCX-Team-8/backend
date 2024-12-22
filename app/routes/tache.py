from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlmodel import Session as SQLSession
from datetime import date
from typing import List, Optional

from ..services.tache import TacheService
from ..models.tache import Tache, TacheAssignee, StatusTache
from ..database import get_session  # Assuming get_session is a dependency for database session

router = APIRouter()

# Create a new task
@router.post("/taches", response_model=Tache, status_code=status.HTTP_201_CREATED)
def create_tache(tache: Tache, session: SQLSession = Depends(get_session)):
    return TacheService.create_tache(session, tache)

# Get a task by ID
@router.get("/taches/{tache_id}", response_model=Tache)
def get_tache_by_id(tache_id: int, session: SQLSession = Depends(get_session)):
    tache = TacheService.get_tache_by_id(session, tache_id)
    if not tache:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return tache

# Get all tasks
@router.get("/taches", response_model=List[Tache])
def get_all_taches(session: SQLSession = Depends(get_session)):
    return TacheService.get_all_taches(session)

# Update a task
@router.put("/taches/{tache_id}", response_model=Tache)
def update_tache(tache_id: int, updates: dict, session: SQLSession = Depends(get_session)):
    tache = TacheService.update_tache(session, tache_id, updates)
    if not tache:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return tache

# Delete a task
@router.delete("/taches/{tache_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tache(tache_id: int, session: SQLSession = Depends(get_session)):
    if not TacheService.delete_tache(session, tache_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return


# Get all tasks assigned to an employee
@router.get("/employes/{employe_id}/taches", response_model=List[Tache])
def get_assigned_tasks(employe_id: int, session: SQLSession = Depends(get_session)):
    tasks = TacheService.get_assigned_tasks(session, employe_id)
    return tasks

# Update the status of an assigned task
@router.put("/taches/{tache_id}/status", response_model=TacheAssignee)
def update_task_status(tache_id: int, status: StatusTache, session: SQLSession = Depends(get_session)):
    tache_assignee = TacheService.update_task_status(session, tache_id, status)
    if not tache_assignee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not assigned or not found")
    return tache_assignee
