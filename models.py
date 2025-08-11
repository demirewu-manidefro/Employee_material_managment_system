from db import db
from datetime import datetime
from flask_login import UserMixin

class Employee(db.Model):
    __tablename__ = 'employees'  # explicit table name, plural

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    grand_father_name = db.Column(db.String(100), nullable=False)  # ✅ NEW
    sex = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(100), nullable=False)  # ✅ NEW
    employment_status = db.Column(db.String(20), nullable=False)  # ✅ NEW (Contract/Permanent)
    phone_number = db.Column(db.String(20), nullable=False)  # ✅ NEW
    status = db.Column(db.String(20), default='active')  # active/left
    project = db.Column(db.String(200))
    borrowed_materials = db.relationship('BorrowedMaterial', backref='employee', lazy=True)
    leave_out_member = db.relationship('LeaveOutMember', backref='employee', uselist=False)
    waiting_return = db.relationship('WaitingReturn', backref='employee', uselist=False)


class Material(db.Model):
    __tablename__ = 'materials'  # explicit plural table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    serial_number = db.Column(db.String(50), nullable=False, unique=True)
    status = db.Column(db.String(20), default='available')

    borrowed_materials = db.relationship('BorrowedMaterial', backref='material', lazy=True)


class BorrowedMaterial(db.Model):
    __tablename__ = 'borrowed_materials'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    material_id = db.Column(db.Integer, db.ForeignKey('materials.id'), nullable=False)
    purpose = db.Column(db.String(255))
    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_returned = db.Column(db.Boolean, default=False)


class LeaveOutMember(db.Model):
    __tablename__ = 'leave_out_members'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    leave_date = db.Column(db.DateTime, default=datetime.utcnow)


class WaitingReturn(db.Model):
    __tablename__ = 'waiting_return'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    added_date = db.Column(db.DateTime, default=datetime.utcnow)
from werkzeug.security import generate_password_hash, check_password_hash
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default="admin") 
