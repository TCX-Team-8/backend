from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine
from dotenv import load_dotenv
import os


load_dotenv()
postgres_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(postgres_url)

def test_connection():
    try:
        
        postgres_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        engine = create_engine(postgres_url)
        print("Connection string created successfully!")
    except Exception as e:
        print(f"Error creating the connection string or engine: {e}")

def main():
    print("Testing database connection...")
    test_connection()

if __name__ == "__main__":
    main()
