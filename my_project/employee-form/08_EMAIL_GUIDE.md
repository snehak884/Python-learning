# Step 8: Email Notification Guide (Reference Only)

This guide explains how to add email confirmation functionality to your Flask application.

**Note:** This is for reference only - you don't need to test this, but it's useful to understand how email functionality works.

---

## Overview

Email functionality allows you to:
- Send confirmation emails to applicants
- Send notifications to admins
- Send reminders or updates

---

## Common Approaches

### 1. **SMTP (Simple Mail Transfer Protocol)**
- Uses email servers (Gmail, Outlook, etc.)
- Requires email credentials
- Free for personal use
- Libraries: `smtplib` (built-in), `Flask-Mail`

### 2. **Email Service Providers**
- Third-party services (SendGrid, Mailgun, AWS SES)
- More reliable for production
- Often free tier available
- Better deliverability
- Libraries: `sendgrid`, `mailgun`, `boto3` (AWS SES)

---

## Method 1: Using Flask-Mail (Simple)

### Step 1: Install Flask-Mail

```bash
pip install Flask-Mail
```

### Step 2: Update requirements.txt

```
Flask-Mail==0.9.1
```

### Step 3: Configure Flask-Mail in app.py

```python
from flask_mail import Mail, Message

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Your email
app.config['MAIL_PASSWORD'] = 'your-app-password'     # App password (not regular password)
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'

# Initialize Mail
mail = Mail(app)
```

### Step 4: Create Email Function

```python
def send_confirmation_email(applicant_email, applicant_name):
    """Send confirmation email to applicant"""
    try:
        msg = Message(
            subject='Application Received - Thank You!',
            recipients=[applicant_email],  # Send to applicant
            body=f'''
            Dear {applicant_name},
            
            Thank you for submitting your job application!
            
            We have received your application and will review it shortly.
            
            Best regards,
            Hiring Team
            ''',
            html=f'''
            <html>
                <body>
                    <h2>Application Received - Thank You!</h2>
                    <p>Dear {applicant_name},</p>
                    <p>Thank you for submitting your job application!</p>
                    <p>We have received your application and will review it shortly.</p>
                    <p>Best regards,<br>Hiring Team</p>
                </body>
            </html>
            '''
        )
        mail.send(msg)
        print(f"Confirmation email sent to {applicant_email}")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
```

### Step 5: Use in Form Submission

```python
@app.route('/submit', methods=['POST'])
def submit_form():
    # ... get form data ...
    
    # Store in database (Step 5 & 6)
    # ... save to database ...
    
    # Send confirmation email (Step 8)
    send_confirmation_email(email, first_name)
    
    return redirect(url_for('success'))
```

---

## Method 2: Using SMTP (Built-in Python)

### Step 1: Import smtplib (Built-in, no install needed)

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
```

### Step 2: Create Email Function

```python
def send_confirmation_email_smtp(applicant_email, applicant_name):
    """Send confirmation email using SMTP"""
    try:
        # Email configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "your-email@gmail.com"
        sender_password = "your-app-password"
        
        # Create message
        message = MIMEMultipart("alternative")
        message["Subject"] = "Application Received - Thank You!"
        message["From"] = sender_email
        message["To"] = applicant_email
        
        # Create the plain-text and HTML version
        text = f"""
        Dear {applicant_name},
        
        Thank you for submitting your job application!
        
        We have received your application and will review it shortly.
        
        Best regards,
        Hiring Team
        """
        
        html = f"""
        <html>
            <body>
                <h2>Application Received - Thank You!</h2>
                <p>Dear {applicant_name},</p>
                <p>Thank you for submitting your job application!</p>
                <p>We have received your application and will review it shortly.</p>
                <p>Best regards,<br>Hiring Team</p>
            </body>
        </html>
        """
        
        # Turn these into MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        
        # Add parts to message
        message.attach(part1)
        message.attach(part2)
        
        # Create secure connection and send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, applicant_email, message.as_string())
        server.quit()
        
        print(f"Confirmation email sent to {applicant_email}")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
```

---

## Method 3: Using SendGrid (Recommended for Production)

### Step 1: Sign up for SendGrid (Free tier available)

- Go to: https://sendgrid.com/
- Create free account (100 emails/day free)

### Step 2: Get API Key

- Dashboard → Settings → API Keys
- Create API Key
- Save the key (you'll only see it once!)

### Step 3: Install SendGrid

```bash
pip install sendgrid
```

### Step 4: Update requirements.txt

```
sendgrid==6.10.0
```

### Step 5: Create Email Function

```python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

def send_confirmation_email_sendgrid(applicant_email, applicant_name):
    """Send confirmation email using SendGrid"""
    try:
        # Get API key from environment variable (for security)
        api_key = os.getenv('SENDGRID_API_KEY', 'your-api-key-here')
        
        message = Mail(
            from_email='your-email@example.com',
            to_emails=applicant_email,
            subject='Application Received - Thank You!',
            html_content=f'''
            <html>
                <body>
                    <h2>Application Received - Thank You!</h2>
                    <p>Dear {applicant_name},</p>
                    <p>Thank you for submitting your job application!</p>
                    <p>We have received your application and will review it shortly.</p>
                    <p>Best regards,<br>Hiring Team</p>
                </body>
            </html>
            '''
        )
        
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(f"Email sent! Status code: {response.status_code}")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
```

### Step 6: Set Environment Variable

```bash
export SENDGRID_API_KEY='your-api-key-here'
```

Or create `.env` file:
```
SENDGRID_API_KEY=your-api-key-here
```

---

## Gmail Setup (For Testing)

### If using Gmail:

1. **Enable 2-Factor Authentication** on your Google account
2. **Generate App Password**:
   - Google Account → Security → 2-Step Verification
   - App passwords → Generate
   - Use this password (not your regular password)

3. **Use in code**:
```python
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-16-character-app-password'  # App password, not regular password
```

---

## Security Best Practices

### ❌ DON'T:
- Hardcode passwords in code
- Commit passwords to git
- Use regular email passwords

### ✅ DO:
- Use environment variables
- Use app passwords (Gmail)
- Use API keys for services
- Add `.env` to `.gitignore`

### Example .env file:
```
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
SENDGRID_API_KEY=your-api-key
```

### Loading .env file:
```python
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
```

---

## Comparison

| Method | Setup | Free Tier | Production Ready | Difficulty |
|--------|-------|-----------|------------------|------------|
| **Flask-Mail (SMTP)** | Easy | Yes (Gmail) | ⚠️ Limited | Easy |
| **SMTP (Built-in)** | Medium | Yes (Gmail) | ⚠️ Limited | Medium |
| **SendGrid** | Medium | Yes (100/day) | ✅ Yes | Medium |
| **Mailgun** | Medium | Yes (100/day) | ✅ Yes | Medium |
| **AWS SES** | Hard | Yes (Limited) | ✅ Yes | Hard |

---

## Recommended Approach

### For Learning/Testing:
- **Flask-Mail with Gmail** - Easy to set up and test

### For Production:
- **SendGrid or Mailgun** - More reliable, better deliverability, free tier available

---

## Integration with Your App

Add email functionality to `app.py`:

```python
@app.route('/submit', methods=['POST'])
def submit_form():
    # Get form data
    first_name = request.form.get('first_name')
    email = request.form.get('email')
    
    # Store in database (Steps 5 & 6)
    # ... save to database ...
    
    # Send confirmation email (Step 8)
    try:
        send_confirmation_email(email, first_name)
        flash('Application submitted! Confirmation email sent.', 'success')
    except Exception as e:
        flash('Application submitted! (Email notification failed)', 'warning')
    
    return redirect(url_for('success'))
```

---

## Summary

Email functionality can be added using:
1. **Flask-Mail** - Simplest for learning
2. **SMTP (built-in)** - More control
3. **SendGrid/Mailgun** - Best for production

**For this project:** Flask-Mail with Gmail is perfect for learning and understanding how email works.

---

## Resources

- Flask-Mail Documentation: https://pythonhosted.org/Flask-Mail/
- SendGrid Documentation: https://docs.sendgrid.com/
- Gmail App Passwords: https://support.google.com/accounts/answer/185833
