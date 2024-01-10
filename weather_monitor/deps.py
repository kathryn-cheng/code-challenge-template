from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from weather_monitor.database_engine import SessionLocal


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionDep = Annotated[Session, Depends(get_db)]
