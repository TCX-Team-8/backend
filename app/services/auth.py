from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ..models.user import Utilisateur
from typing import Optional


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Utilisateur:
        return db.query(Utilisateur).filter(Utilisateur.email == email).first()
