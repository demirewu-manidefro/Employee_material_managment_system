import os

class Config:
    # Use DATABASE_URL from environment if available
    uri = os.environ.get("DATABASE_URL", "postgresql://postgres:ahati21+@localhost:5432/employee_db")

    # Ensure psycopg2 driver and sslmode=require
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql+psycopg2://", 1)
    elif uri.startswith("postgresql://"):
        uri = uri.replace("postgresql://", "postgresql+psycopg2://", 1)

    SQLALCHEMY_DATABASE_URI = uri + ("?sslmode=require" if "sslmode" not in uri else "")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "my-secret-key")
