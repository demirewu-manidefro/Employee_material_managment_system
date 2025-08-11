from app import app
from db import db
from models import User
from werkzeug.security import generate_password_hash

with app.app_context():
    username = "admin"
    password = "admin123"
    role = "admin"

    if User.query.filter_by(username=username).first():
        print(f"❌ User '{username}' already exists.")
    else:
        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw, role=role)
        db.session.add(new_user)
        db.session.commit()
        print(f"✅ User '{username}' created successfully.")
