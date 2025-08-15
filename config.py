import os

class Config:
    # Use the DATABASE_URL from Render environment variables
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for Flask sessions
    SECRET_KEY = os.environ.get('SECRET_KEY')