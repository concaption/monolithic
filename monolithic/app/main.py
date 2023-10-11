"""
path: monolithic/app/main.py

"""

from app.api.api import api_router
from app.core.config import DATABASE_URL
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Database setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()

# Include API routers
app.include_router(api_router, prefix="/api")


# Dependency to get the database session
def get_db():
    """Get the database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
