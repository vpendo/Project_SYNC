from fastapi import Depends
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, Base  # Adjusted import
from typing import Annotated

# Ensure all tables are created
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]