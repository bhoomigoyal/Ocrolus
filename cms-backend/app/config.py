
# app/config.py
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/cms")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "changeme")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

settings = Settings()
