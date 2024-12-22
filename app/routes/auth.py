from datetime import date
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from passlib.context import CryptContext
from ..models.user import Utilisateur  # Assuming your model is in models/utilisateur.py
from ..services.auth import AuthService  # Assuming you have a service handling auth logic
from ..database import get_session
from typing import Optional


router = APIRouter()

# Password hashing and verification with passlib
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserCreate(BaseModel):
    nom: str
    prenom: str
    email: str
    tel: str
    tel_urgence: str
    lien_urgence: str
    nss: str
    adresse: str
    date_naissance: date  
    departement_id: Optional[int]
    photo: str
    mot_de_passe: str
    matricule: str

class LoginRequest(BaseModel):
    email: str
    mot_de_passe: str

class UserResponse(BaseModel):
    id: int
    nom: str
    prenom: str
    email: str

# Route to register a new user
@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, session: Session = Depends(get_session)):
    # Check if the email already exists
    existing_user = session.query(Utilisateur).filter(Utilisateur.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    # Hash password
    hashed_password = pwd_context.hash(user.mot_de_passe)
    user_data = user.dict()
    user_data['mot_de_passe'] = hashed_password

    # Create the user and save to the database
    new_user = Utilisateur(**user_data)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    
    return new_user

# Route to login a user
@router.post("/login")
def login_user(login: LoginRequest, session: Session = Depends(get_session)):
    # Get the user by email
    user = session.query(Utilisateur).filter(Utilisateur.email == login.email).first()
    
    if not user or not pwd_context.verify(login.mot_de_passe, user.mot_de_passe):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")
    
    # Here you could return a JWT token for session management
    return {"msg": "Login successful", "user_id": user.id}

# Route to check the authentication status (this can be improved with JWT or OAuth)
@router.get("/status", response_model=UserResponse)
def get_auth_status(session: Session = Depends(get_session)):
    # Example of checking the authenticated user, in a real-world app this would be tied to a JWT
    user = session.query(Utilisateur).first()  # You'd normally get the current user from the token/session
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    return user
