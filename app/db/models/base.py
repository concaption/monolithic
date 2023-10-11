"""
path: app/db/models/base.py
"""

from enum import Enum as PyEnum

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class UserRole(PyEnum):
    """Enum for user roles"""

    employer = "employer"
    candidate = "candidate"
    admin = "admin"


class User(Base):
    """User model"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(Enum(UserRole))
    jobs = relationship("Job", back_populates="employer")
    applications = relationship("Application", back_populates="candidate")
    profile = relationship("Profile", uselist=False, back_populates="user")


class Job(Base):
    """Job model"""

    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    employer_id = Column(Integer, ForeignKey("users.id"))
    is_approved = Column(Boolean, default=False)
    employer = relationship("User", back_populates="jobs")
    applications = relationship("Application", back_populates="job")


class Application(Base):
    """Application model"""

    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    candidate_id = Column(Integer, ForeignKey("users.id"))
    job = relationship("Job", back_populates="applications")
    candidate = relationship("User", back_populates="applications")


class Profile(Base):
    """Profile model"""

    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    bio = Column(String)
    experience = Column(String)
    skills = Column(String)
    user = relationship("User", back_populates="profile")
