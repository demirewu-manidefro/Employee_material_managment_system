
import os

class Config:
    # Get the database URL from environment
    uri = os.getenv("DATABASE_URL", "")

    # Fix "postgres://" → "postgresql://"
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    # Ensure sslmode=require for Render Postgres
    if uri and "sslmode" not in uri:
        uri += "?sslmode=require"

    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret")

