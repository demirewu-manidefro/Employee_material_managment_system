import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # reads the env variable
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_secret')
