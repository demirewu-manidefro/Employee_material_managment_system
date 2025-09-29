import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:ahati21%2B@dpg-d2fpac24d50c73b43ve0-a.oregon-postgres.render.com/dbems_project_db?sslmode=require'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
