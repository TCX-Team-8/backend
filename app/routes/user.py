from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from ..services.user import UtilisateurService
from ..models.user import Utilisateur
from ..schemas.user import UtilisateurCreate
from ..database import get_session


user_router = APIRouter()

# Route to create a new user
@user_router.post("/", response_model=Utilisateur)
def create_utilisateur(user: UtilisateurCreate, session: Session = Depends(get_session)):
    new_user = Utilisateur(**user.model_dump())
    created_user = UtilisateurService.create_utilisateur(session, new_user)
    return created_user

# Route to get all users
@user_router.get("/")
def get_all_utilisateurs(session: Session = Depends(get_session)):
    all_users = UtilisateurService.get_all_utilisateurs(session)
    return all_users

# Route to update a user
@user_router.put("/{user_id}", response_model=Utilisateur)
def update_utilisateur(user_id: int, user: UtilisateurCreate, session: Session = Depends(get_session)):
    updates = user.model_dump(exclude_unset=True)
    updated_user = UtilisateurService.update_utilisateur(session, user_id, updates)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

# Route to delete a user
@user_router.delete("/{user_id}")
def delete_utilisateur(user_id: int, session: Session = Depends(get_session)):
    UtilisateurService.delete_utilisateur(session, user_id)
    return {"message": "User deleted"}
