"""
Flask-WTF Forms
Form validation and structure
"""

from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, DateField, RadioField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from datetime import date


class JobApplicationForm(FlaskForm):
    """Job application form with validation"""
    
    first_name = StringField(
        'First Name',
        validators=[
            DataRequired(message='First name is required'),
            Length(min=2, max=100, message='First name must be between 2 and 100 characters')
        ],
        render_kw={"placeholder": "Enter your first name", "class": "form-control"}
    )
    
    last_name = StringField(
        'Last Name',
        validators=[
            DataRequired(message='Last name is required'),
            Length(min=2, max=100, message='Last name must be between 2 and 100 characters')
        ],
        render_kw={"placeholder": "Enter your last name", "class": "form-control"}
    )
    
    email = EmailField(
        'Email',
        validators=[
            DataRequired(message='Email is required'),
            Email(message='Please enter a valid email address'),
            Length(max=120, message='Email must be less than 120 characters')
        ],
        render_kw={"placeholder": "your.email@example.com", "class": "form-control"}
    )
    
    start_date = DateField(
        'Available Start Date',
        validators=[
            DataRequired(message='Start date is required')
        ],
        render_kw={"class": "form-control"}
    )
    
    occupation = RadioField(
        'Current Occupation',
        choices=[
            ('employed', 'Employed'),
            ('unemployed', 'Unemployed'),
            ('self-employed', 'Self-Employed'),
            ('student', 'Student')
        ],
        validators=[
            DataRequired(message='Please select your occupation')
        ]
    )
    
    submit = SubmitField(
        'Submit Application',
        render_kw={"class": "btn btn-primary btn-lg"}
    )
    
    def validate_start_date(self, field):
        """Validate that start date is in the future"""
        if field.data and field.data < date.today():
            raise ValidationError('Start date must be today or in the future')
    
    def validate_email(self, field):
        """Additional email validation"""
        email = field.data
        if email:
            # Basic email format check (WTForms already does this, but adding extra validation)
            if '@' not in email or '.' not in email.split('@')[1]:
                raise ValidationError('Please enter a valid email address')
