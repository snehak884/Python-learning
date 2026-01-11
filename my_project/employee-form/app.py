"""
Flask Employee Form Application
Improved version with security, validation, and admin panel
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Import configuration
from config import config

# Initialize Flask app
app = Flask(__name__)

# Apply configuration
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

# Initialize database
db = SQLAlchemy(app)

# Database Model (Step 5)
class Employee(db.Model):
    """Employee/Application model for database"""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    start_date = db.Column(db.String(20), nullable=False)
    occupation = db.Column(db.String(50), nullable=False)
    submission_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    def __repr__(self):
        return f'<Employee {self.first_name} {self.last_name} - {self.email}>'
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'start_date': self.start_date,
            'occupation': self.occupation,
            'submission_date': self.submission_date.strftime('%Y-%m-%d %H:%M:%S') if self.submission_date else None
        }

# Import forms
try:
    from forms import JobApplicationForm
    FLASK_WTF_AVAILABLE = True
except ImportError:
    FLASK_WTF_AVAILABLE = False
    print("Note: Flask-WTF not installed. Using basic form validation.")


@app.route('/')
def index():
    """Home page - display the form"""
    if FLASK_WTF_AVAILABLE:
        form = JobApplicationForm()
        return render_template('index.html', form=form)
    else:
        return render_template('index.html', form=None)


@app.route('/submit', methods=['POST'])
def submit_form():
    """Handle form submission with validation"""
    
    if FLASK_WTF_AVAILABLE:
        form = JobApplicationForm()
        if not form.validate_on_submit():
            # Form validation failed
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'{getattr(form, field).label.text}: {error}', 'danger')
            return redirect(url_for('index'))
        
        # Get validated form data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        start_date = form.start_date.data.strftime('%Y-%m-%d')
        occupation = form.occupation.data
    else:
        # Fallback to basic validation
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        email = request.form.get('email', '').strip()
        start_date = request.form.get('start_date', '')
        occupation = request.form.get('occupation', '')
        
        # Basic validation
        if not all([first_name, last_name, email, start_date, occupation]):
            flash('Please fill in all required fields.', 'danger')
            return redirect(url_for('index'))
        
        if '@' not in email or '.' not in email.split('@')[1]:
            flash('Please enter a valid email address.', 'danger')
            return redirect(url_for('index'))
    
    # Step 5: Store in database
    try:
        # Check if email already exists
        existing_employee = Employee.query.filter_by(email=email).first()
        if existing_employee:
            flash('This email has already been used. Please use a different email address.', 'warning')
            return redirect(url_for('index'))
        
        # Create new employee record
        new_employee = Employee(
            first_name=first_name,
            last_name=last_name,
            email=email,
            start_date=start_date,
            occupation=occupation
        )
        
        # Add to database
        db.session.add(new_employee)
        db.session.commit()
        
        # Print for testing (optional)
        print(f"\n=== Application Saved ===")
        print(f"Name: {first_name} {last_name}")
        print(f"Email: {email}")
        print(f"Start Date: {start_date}")
        print(f"Occupation: {occupation}")
        print(f"Saved to database with ID: {new_employee.id}")
        print("=========================\n")
        
        # Step 7: Show success message
        flash(f'Application submitted successfully! Thank you {first_name}.', 'success')
        
        # TODO: Step 8 - Send confirmation email (reference only - see 08_EMAIL_GUIDE.md)
        
        return redirect(url_for('success'))
        
    except Exception as e:
        # If there's an error
        db.session.rollback()
        print(f"Error saving to database: {e}")
        flash('There was an error submitting your application. Please try again.', 'danger')
        return redirect(url_for('index'))


@app.route('/success')
def success():
    """Success page after form submission"""
    return render_template('success.html')


@app.route('/admin')
def admin():
    """Admin panel - view all applications"""
    # Simple password protection (basic - not for production!)
    password = request.args.get('password', '')
    
    if password != config.ADMIN_PASSWORD:
        flash('Please enter the admin password to view applications.', 'warning')
        return render_template('admin_login.html')
    
    # Get all applications
    try:
        applications = Employee.query.order_by(Employee.submission_date.desc()).all()
        total_count = len(applications)
        
        return render_template('admin.html', applications=applications, total_count=total_count)
    except Exception as e:
        print(f"Error loading applications: {e}")
        flash('Error loading applications.', 'danger')
        return redirect(url_for('index'))


@app.route('/admin/delete/<int:employee_id>', methods=['POST'])
def delete_application(employee_id):
    """Delete an application (admin only)"""
    password = request.form.get('password', '')
    
    if password != config.ADMIN_PASSWORD:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('index'))
    
    try:
        employee = Employee.query.get_or_404(employee_id)
        db.session.delete(employee)
        db.session.commit()
        flash(f'Application from {employee.email} has been deleted.', 'success')
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting application: {e}")
        flash('Error deleting application.', 'danger')
    
    return redirect(url_for('admin', password=config.ADMIN_PASSWORD))


@app.route('/api/applications')
def api_applications():
    """API endpoint - get all applications as JSON"""
    try:
        applications = Employee.query.order_by(Employee.submission_date.desc()).all()
        return jsonify({
            'success': True,
            'count': len(applications),
            'applications': [app.to_dict() for app in applications]
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.errorhandler(404)
def not_found(error):
    """Custom 404 error page"""
    return render_template('error.html', error_code=404, error_message='Page not found'), 404


@app.errorhandler(500)
def internal_error(error):
    """Custom 500 error page"""
    db.session.rollback()
    return render_template('error.html', error_code=500, error_message='Internal server error'), 500


if __name__ == '__main__':
    # Step 5: Create database tables
    with app.app_context():
        db.create_all()
        print("Database initialized!")
    
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=5000)
