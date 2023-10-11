"""
path: app/main.py

"""

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from app.api.api import api_router
from app.core.config import DATABASE_URL

app = FastAPI()


# Include API routers
app.include_router(api_router, prefix="/api")
