"""
View Applications Script (Optional - for testing)
Step 5: View stored applications in database
"""

from app import app as flask_app, db
from app import Employee
from datetime import datetime

def view_all_applications():
    """View all applications in database"""
    with flask_app.app_context():
        applications = Employee.query.all()
        
        if not applications:
            print("\n=== No Applications Found ===")
            print("Database is empty. Submit a form to add applications.\n")
            return
        
        print("\n=== All Applications ===")
        print(f"Total Applications: {len(applications)}\n")
        
        for employee in applications:  # Changed 'app' to 'employee' to avoid naming conflict
            print(f"ID: {employee.id}")
            print(f"Name: {employee.first_name} {employee.last_name}")
            print(f"Email: {employee.email}")
            print(f"Start Date: {employee.start_date}")
            print(f"Occupation: {employee.occupation}")
            print(f"Submitted: {employee.submission_date}")
            print("-" * 40)
        
        print("\n")

if __name__ == '__main__':
    view_all_applications()
