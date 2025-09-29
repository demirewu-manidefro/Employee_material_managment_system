
import os

class Config:
    uri = os.getenv("DATABASE_URL", "")

    # Fix double "postgresql://postgresql"
    if uri.startswith("postgresql://postgresql"):
        uri = uri.replace("postgresql://postgresql", "postgresql://postgres", 1)

    # Fix old "postgres://" style URLs
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    # Always enforce sslmode=require
    if uri and "sslmode" not in uri:
        if "?" in uri:
            uri += "&sslmode=require"
        else:
            uri += "?sslmode=require"

    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret")
