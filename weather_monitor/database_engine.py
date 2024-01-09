from sqlalchemy.orm import sessionmaker, declarative_base

from weather_monitor.config import settings
from sqlalchemy import create_engine

# Database Configuration
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI.unicode_string()
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()