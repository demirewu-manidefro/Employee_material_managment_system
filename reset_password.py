from app import app, db
from models import User  # adjust if your User model is elsewhere
from werkzeug.security import generate_password_hash

with app.app_context():
    username_to_reset = 'admin'  # change if needed
    new_password = 'NewPass123!'

    u = User.query.filter_by(username=username_to_reset).first()
    if not u:
        print("User not found. Change the username in the script and try again.")
    else:
        u.password = generate_password_hash(new_password)
        db.session.commit()
        print(f"Password for {u.username} reset to {new_password}")
