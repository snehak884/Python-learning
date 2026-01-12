# Employee Form Application - Flask Project

A step-by-step Flask web application for collecting job application forms.

---

## 📁 Project Files

### Essential Files:
- ✅ `app.py` - **FLASK BACKEND** - Main Flask application (Step 4)
- ✅ `requirements.txt` - Python dependencies (install these!)
- ✅ `templates/index.html` - HTML form with Bootstrap styling
- ✅ `templates/success.html` - Success page after submission
- ✅ `SETUP_INSTRUCTIONS.md` - How to setup and run Flask app
- ✅ `00_FLASK_DJANGO_GUIDE.md` - Flask vs Django explanation (reference)
- ✅ `08_EMAIL_GUIDE.md` - Email functionality guide (reference only)
- ✅ `README.md` - This file (project overview)

### Coming Next:
- ⏭️ Database models (Step 5)
- ⏭️ Database storage (Step 6)

---

## 🚀 Quick Start - Testing the Form

### Step 1: Test the HTML Form (NOW)

**Method 1: Direct Browser Open (Easiest)**
1. Navigate to this folder: `my_project/employee-form/`
2. **Double-click `index.html`**
3. The form opens in your browser!

**Method 2: Using Python Server**
```bash
cd my_project/employee-form
python3 -m http.server 8000
```
Then open: http://localhost:8000/

**What to check:**
- ✅ Form looks good with Bootstrap styling
- ✅ All fields are visible (First Name, Last Name, Email, Date, Occupation)
- ✅ Submit button is there
- ⚠️ Submit won't work yet (no backend - that's next!)

---

## 📋 Project Steps (Step by Step)

### ✅ Step 1: Understanding Flask and Django
- See `00_FLASK_DJANGO_GUIDE.md`

### ✅ Step 2: Create HTML Page
- **DONE!** - `index.html` is ready
- **ACTION: Test it now!**

### ✅ Step 3: Bootstrap Styling
- **DONE!** - Already included in `index.html`

### ✅ Step 4: Create Flask Backend
- ✅ Created `app.py` - Flask application
- ✅ Created `templates/` folder - HTML templates
- ✅ Created `success.html` - Success page
- ✅ Form submission handling ready
- **Next: Test the Flask app, then setup database**

### ✅ Step 5: Setup Database
- ✅ SQLAlchemy setup
- ✅ Database model created (Employee)
- ✅ Database tables initialized
- ✅ Form data saved to database

### ✅ Step 6: Store Form Data
- ✅ Database integration complete
- ✅ Form submissions saved automatically
- ✅ Data persistence working

### ⏭️ Step 7: Show Submission Notification
- User feedback
- Success messages

### ⏭️ Step 8: Send Confirmation Email
- Email functionality (reference only - see `08_EMAIL_GUIDE.md`)
- Confirmation emails
- **Note:** Guide created, but won't be tested

---

## 🎯 Current Status

- ✅ HTML form created
- ✅ Bootstrap styling applied
- ✅ Flask backend created (`app.py`)
- ✅ Templates folder created
- ✅ Success page created
- ⏭️ **NEXT: Install dependencies and test Flask app, then setup database**

---

## 📝 Notes

- The form currently has **no backend**, so submission won't work yet
- This is just the **frontend** (HTML/CSS) right now
- **Next step:** Create Flask backend to handle form submission
- See `TESTING_INSTRUCTIONS.md` for detailed testing guide

---

## 📚 Reference Files

- `00_FLASK_DJANGO_GUIDE.md` - Learn about Flask vs Django
- `TESTING_INSTRUCTIONS.md` - Detailed testing instructions


Here’s what to test:

## What to test now

### Step 4: Test the Flask backend

Flask is not installed yet. Follow these steps:

#### Step 1: Install dependencies
```bash
cd /Users/sneha/Desktop/python-code/my_project/employee-form
pip3 install -r requirements.txt
```

This installs Flask, Flask-SQLAlchemy, and Werkzeug.

#### Step 2: Run the Flask app
```bash
python3 app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

#### Step 3: Open in browser
Open: http://localhost:5000/

#### Step 4: Test the form
1. The form should load
2. Fill out all fields (First Name, Last Name, Email, Date, Occupation)
3. Click "Submit Application"
4. You should see the success page
5. Check your terminal — the form data should be printed there

---

## What to check

- Form displays correctly
- All fields work
- Submit button works
- Success page shows after submission
- Form data appears in terminal (for testing)

Note: Data isn’t saved to a database yet — that’s Step 5.

---

## Summary

Test: Flask backend (Step 4)

Actions:
1. Install: `pip3 install -r requirements.txt`
2. Run: `python3 app.py`
3. Open: http://localhost:5000/
4. Submit the form and check the success page and terminal output

Ready for Step 5 (Database) once this is working.


Checking the current setup and recommending whether to use a virtual environment:


[4 tools called]


## Should you use .venv?

### Quick answer
- Optional for quick testing — you can skip it and install Flask directly
- Recommended for best practice — keeps dependencies isolated

### Recommendation
For now, skip the virtual environment to test faster. You can use one later for better organization.

---

## Option 1: Skip virtual environment (fastest)

Just install Flask directly:

```bash
cd /Users/sneha/Desktop/python-code/my_project/employee-form
pip3 install -r requirements.txt
python3 app.py
```

Pros: fast, simple  
Cons: installs packages globally

---

## Option 2: Use virtual environment (recommended)

If you want to use one:

```bash
cd /Users/sneha/Desktop/python-code/my_project/employee-form

# Create virtual environment
python3 -m venv .venv

# Activate it (Mac/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# When done, deactivate
deactivate
```

Pros: clean, isolated, good practice  
Cons: extra setup step

---

## What I recommend

Skip the virtual environment for now to test quickly. You can always add one later.

### Steps to test now (without .venv):

```bash
cd /Users/sneha/Desktop/python-code/my_project/employee-form
pip3 install -r requirements.txt
python3 app.py
```

Then open: http://localhost:5000/

---

## Summary

- Skip .venv for now — test faster
- Use .venv later — better organization (optional)

Install Flask directly, test the app, and continue. You can add a virtual environment later if needed.


Flask app is working. Proceeding to Step 5: Database setup. Creating the database model and updating the app to save form data.


[16 tools called]


Completed Steps 5, 6, and 7: Database Setup, Data Storage, and Notifications.

## What was added

### Step 5 & 6: Database setup and data storage
- Created `Employee` database model
- Database initialization (creates `data.db` on first run)
- Form data saved to database automatically
- Error handling for duplicate emails

### Step 7: Notifications
- Flash messages added to the form page
- Success/error messages working
- User feedback implemented

### Bonus file
- `view_applications.py` - Optional script to view all stored applications

---

## What to test next

### Step 1: Restart the Flask app
```bash
cd /Users/sneha/Desktop/python-code/my_project/employee-form
python3 app.py
```

### Step 2: Test the database
1. Open: http://localhost:5000/
2. Fill out the form
3. Submit the application
4. You should see:
   - Success message on the form (if error) or success page
   - Data saved in the terminal output
   - Database file created (`data.db`)

### Step 3: View stored applications (optional)
In a new terminal:
```bash
cd /Users/sneha/Desktop/python-code/my_project/employee-form
python3 view_applications.py
```
This shows all stored applications.

---

## What to check

- Database file created (`data.db` in the project folder)
- Form data saved (check terminal output)
- Success messages appear
- Multiple submissions saved correctly
- Duplicate email handled (try submitting the same email twice)

---

## Project status

- Step 1-3: HTML form — complete
- Step 4: Flask backend — complete
- Step 5: Database setup — complete
- Step 6: Data storage — complete
- Step 7: Notifications — complete
- Step 8: Email guide — reference only (`08_EMAIL_GUIDE.md`)

---

## Summary

Test: Database functionality (Steps 5, 6, 7)

Actions:
1. Restart: `python3 app.py`
2. Submit: Fill out and submit the form
3. Check: See data saved in terminal
4. Verify: Database file created (`data.db`)
5. Optional: Run `view_applications.py` to see all stored data

All core functionality is complete. The app now saves form data to a database and shows notifications. Test it and let me know if everything works.



## 1. Database module — SQLAlchemy

Yes, we're using Flask-SQLAlchemy (SQLAlchemy) for the database. It's an ORM (Object-Relational Mapping) that works with different databases.

### Current setup (SQLite)
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
```
- SQLite is built-in, no separate server needed
- Good for development and small projects
- Single file database (`data.db`)

---

## How to use PostgreSQL instead

### Step 1: Install PostgreSQL libraries
```bash
pip install psycopg2-binary
```
OR
```bash
pip install psycopg2
```

### Step 2: Update `app.py` configuration
Change this line in `app.py`:
```python
# OLD (SQLite):
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# NEW (PostgreSQL):
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/database_name'
```

### PostgreSQL connection format:
```
postgresql://username:password@host:port/database_name
```

Example:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@localhost:5432/employee_db'
```

### Step 3: Update requirements.txt
Add:
```
psycopg2-binary==2.9.9
```

### Step 4: No code changes needed
The same code works:
- Your `Employee` model stays the same
- Your database operations stay the same
- Only the connection string changes

---

## Comparison: SQLite vs PostgreSQL

| Feature | SQLite | PostgreSQL |
|---------|--------|------------|
| Setup | No setup needed | Requires installation |
| Server | No server needed | Requires database server |
| Good For | Development, small apps | Production, large apps |
| Connection | File-based | Server-based |
| Speed | Fast for small data | Fast for large data |
| Concurrent Users | Limited | Better support |

Recommendation: Use SQLite for development/learning, PostgreSQL for production.

---

## 2. Email code — where to add it

Email code isn't implemented yet. The email guide (`08_EMAIL_GUIDE.md`) has examples. Here's how to add it:

### Where to add email code

In `app.py`, in the `submit_form()` function, after saving to database:

```python
@app.route('/submit', methods=['POST'])
def submit_form():
    # ... get form data ...
    
    # Step 5: Store in database
    try:
        # ... save to database ...
        
        # Step 8: Send confirmation email (ADD HERE)
        try:
            send_confirmation_email(email, first_name)
            print(f"Confirmation email sent to {email}")
        except Exception as e:
            print(f"Email error: {e}")
            # Continue anyway - email failure shouldn't break form submission
        
        flash('Application submitted successfully!', 'success')
        return redirect(url_for('success'))
    except Exception as e:
        # ... error handling ...
```

### Step-by-step to add email

1. Install Flask-Mail (or SendGrid):
   ```bash
   pip install Flask-Mail
   ```

2. Add to requirements.txt:
   ```
   Flask-Mail==0.9.1
   ```

3. Add email configuration to `app.py` (after Flask app initialization):
   ```python
   from flask_mail import Mail, Message
   
   # Email configuration (add after app.config)
   app.config['MAIL_SERVER'] = 'smtp.gmail.com'
   app.config['MAIL_PORT'] = 587
   app.config['MAIL_USE_TLS'] = True
   app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
   app.config['MAIL_PASSWORD'] = 'your-app-password'  # Gmail app password
   app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'
   
   mail = Mail(app)
   ```

4. Create email function (add before routes):
   ```python
   def send_confirmation_email(applicant_email, applicant_name):
       """Send confirmation email to applicant"""
       try:
           msg = Message(
               subject='Application Received - Thank You!',
               recipients=[applicant_email],
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
           return True
       except Exception as e:
           print(f"Error sending email: {e}")
           return False
   ```

5. Call the function in `submit_form()` (after saving to database):
   ```python
   # After db.session.commit()
   send_confirmation_email(email, first_name)
   ```

---

## Quick summary

### Database (PostgreSQL):
- Change only the connection string in `app.py`
- Install `psycopg2-binary`
- Everything else stays the same

### Email:
- Add configuration to `app.py`
- Create `send_confirmation_email()` function
- Call it in `submit_form()` after database save
- See `08_EMAIL_GUIDE.md` for more details and alternatives

Both are straightforward to add when needed.


more info : https://dailypythonprojects.substack.com/t/api

