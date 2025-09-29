import os

class Config:
    uri = os.getenv("DATABASE_URL", "")

    # Fix accidental "postgresql://postgresql" prefix
    if uri.startswith("postgresql://postgresql"):
        uri = uri.replace("postgresql://postgresql", "postgresql://postgres", 1)

    # Convert legacy "postgres://" to "postgresql://"
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    # Ensure sslmode=require
    if uri and "sslmode" not in uri:
        if "?" in uri:
            uri += "&sslmode=require"
        else:
            uri += "?sslmode=require"

    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Give SQLAlchemy engine explicit connect_args and a small pool to avoid connection limits
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {"sslmode": "require"},
        "pool_size": 3,
        "max_overflow": 2,
        "pool_timeout": 30,
        "pool_recycle": 1800
    }

    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret")
