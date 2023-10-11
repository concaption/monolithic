"""
path: app/services/auth.py
"""
from datetime import datetime, timedelta

from core.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.db.models.base import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
outh2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    """Verify password"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Get password hash"""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta = None):
    """Create access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    """Decode access token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")


def get_current_user(db, token: str = Security(outh2_scheme)):
    """Get current user"""
    payload = decode_access_token(token)
    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    return user


def get_current_user_role(current_user: User = Security(get_current_user)):
    """Get current user role"""
    return current_user.role
