"""
path: app/services/crud.py
"""

from db.models.base import Application, Job, Profile, User
from sqlalchemy.orm import Session

from app.services.auth import get_password_hash


# User CRUD
def create_user(db: Session, username: str, email: str, password: str, role: str):
    """Create user"""
    db_user = User(
        username=username, email=email, password=get_password_hash(password), role=role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_id(db: Session, user_id: int):
    """Get user by id"""
    return db.query(User).filter(User.id == user_id).first()


# Job CRUD
def create_job(db: Session, title: str, description: str, employer_id: int):
    """Create job"""
    db_job = Job(title=title, description=description, employer_id=employer_id)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    """Get jobs"""
    return db.query(Job).offset(skip).limit(limit).all()


# Application CRUD
def create_application(db: Session, job_id: int, candidate_id: int):
    """Create application"""
    db_application = Application(job_id=job_id, candidate_id=candidate_id)
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application


def get_applications_by_job_id(db: Session, job_id: int):
    """Get applications by job id"""
    return db.query(Application).filter(Application.job_id == job_id).all()


# Profile CRUD
def create_profile(db: Session, user_id: int, bio: str, experience: str, skills: str):
    """Create profile"""
    db_profile = Profile(user_id=user_id, bio=bio, experience=experience, skills=skills)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def get_profile_by_user_id(db: Session, user_id: int):
    """Get profile by user id"""
    return db.query(Profile).filter(Profile.user_id == user_id).first()
