"""
path: api/routes/employers.py

"""

from db.models.base import Job, User
from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException
from services.auth import UserRoles, get_current_user, get_current_user_role
from services.crud import create_job, get_jobs
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/jobs/", response_model=Job, name="jobs:create-job")
async def create_new_job(
    title: str,
    description: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Create a new job
    """
    if get_current_user_role(current_user) == UserRoles.employer:
        job = create_job(
            db, title=title, description=description, employer_id=current_user.id
        )
        return job
    raise HTTPException(status_code=400, detail="Not authorized")


@router.get("/jobs/", response_model=list[Job], name="jobs:get-jobs")
async def get_all_jobs(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Get all jobs
    """
    if get_current_user_role(current_user) == UserRoles.employer:
        jobs = get_jobs(db, skip=skip, limit=limit)
        return jobs
    raise HTTPException(status_code=400, detail="Not authorized")
