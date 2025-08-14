# config.py
import os

class Config:
    # Get DB URL from environment variable, fallback to local DB
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:ahati21%2B@localhost/ems_project_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Get secret key from environment variable, fallback to local value
    SECRET_KEY = os.environ.get(
        'SECRET_KEY',
        '3a9c21b1b4f3420e8d1fdd5935d60fd0e3b03f8b0b36f428b2d3c1f23ef29b51'
    )
