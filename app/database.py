from sqlmodel import create_engine, SQLModel
from dotenv import load_dotenv
import os

# Import all models to ensure they are registered with SQLModel
from models.user import Utilisateur, Departement, RH, Admin, Employe
from models.tache import Tache, TacheAssignee
from models.pointage import Pointage, Absence, Retard
from models.notification import Notification, Rappel, AvertissementAbsence, AvertissementRetard
from models.seuil import Seuil
from models.conge import Conge

load_dotenv()

# Define the PostgreSQL URL
postgres_url = f"postgresql://postgres:123456@localhost:5432/TCX"
print(f"Postgres URL: {postgres_url}")

# Create the engine
engine = create_engine(postgres_url)

def create_tables():
    try:
        # Drop tables before creating them (use carefully, especially in production)
        SQLModel.metadata.drop_all(engine)
        
        # Create all tables (order should be resolved through SQLModel's metadata)
        SQLModel.metadata.create_all(engine)
        print("Database and tables created successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")

def test_connection():
    try:
        print("Connection string created successfully!")
        create_tables()
    except Exception as e:
        print(f"Error creating the connection string or engine: {e}")

if __name__ == "__main__":
    test_connection()
