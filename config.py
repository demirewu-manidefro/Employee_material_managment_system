import os

class Config:
    # Use DATABASE_URL from environment if available, otherwise fallback to local Postgres
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql://postgres:ahati21+@localhost:5432/employee_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "my-secret-key")
