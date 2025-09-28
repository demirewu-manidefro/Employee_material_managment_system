import os

class Config:
    # Database URL
    SQLALCHEMY_DATABASE_URI = "postgresql://dbems_project_db_m2eo_user:mkZcPoxsm2XMCRO9RYXuSll92OANARp9@dpg-d39p6njuibrs73f1if90-a.oregon-postgres.render.com/dbems_project_db_m2eo?sslmode=require"
    
    # Disable modification tracking (recommended)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask secret key
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')
