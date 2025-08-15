import os

class Config:
    # Use DATABASE_URL from environment variables, fallback to the correct Render DB URL
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgresql:IZKgRHdcMNqMjX0Yvf95o8FNOKTDkHm1@dpg-d2fpac24d50c73b43ve0-a.oregon-postgres.render.com/dbems_project_db'
    ).strip()  # <-- remove any accidental whitespace or newline
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for Flask sessions
    SECRET_KEY = os.environ.get(
        'SECRET_KEY',
        '3a9c21b1b4f3420e8d1fdd5935d60fd0e3b03f8b0b36f428b2d3c1f23ef29b51'
    ).strip()  # <-- remove whitespace if any
