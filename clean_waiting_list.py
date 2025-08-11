# from app import app
# from db import db
# from models import WaitingReturn, Employee, BorrowedMaterial

# with app.app_context():
#     waiting_members = WaitingReturn.query.all()

#     for member in waiting_members:
#         employee = Employee.query.get(member.employee_id)

#         if not employee:
#             print(f"❌ Employee with ID {member.employee_id} does not exist. Deleting from waiting list...")
#             db.session.delete(member)
#             continue

#         borrowings = BorrowedMaterial.query.filter_by(employee_id=employee.id, is_returned=False).all()

#         if not borrowings:
#             print(f"✅ {employee.name} ({employee.id}) has returned all items. Removing from waiting list.")
#             db.session.delete(member)

#     db.session.commit()
#     print("🎉 Waiting list cleaned successfully.")
