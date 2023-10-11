"""
path: app/core/config.py

"""
import os

from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Security
SECRET_KEY = os.getenv("SECRET_KEY", "my_precious_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# CORS (optional)
ALLOWED_HOSTS = ["*"]
