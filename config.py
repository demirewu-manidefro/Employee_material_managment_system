import os
from urllib.parse import urlparse

class Config:
# Get DATABASE_URL from environment
    uri = os.environ.get("DATABASE_URL", "postgresql://postgres:ahati21+@localhost:5432/employee_db")


    # Render sets DATABASE_URL without sslmode by default
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    # Add sslmode=require for production
    if "render.com" in uri or "sslmode" not in uri:
        if "?" in uri:
            uri = f"{uri}&sslmode=require"
        else:
            uri = f"{uri}?sslmode=require"

    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "my-secret-key")

