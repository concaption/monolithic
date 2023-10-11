"""
path: monolithic/app/db/session.py

"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import DATABASE_URL

# Intitialize database engine
engine = create_engine(DATABASE_URL)

# Create a custion sessoion class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base model class
Base: DeclarativeMeta = declarative_base()


# Dependency to get the database session
def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
