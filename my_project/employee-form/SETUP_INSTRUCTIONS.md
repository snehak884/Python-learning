# Flask Backend Setup Instructions

## Step 4: Create Flask Backend ✅

The Flask backend has been created! Here's what was added:

### New Files:
- ✅ `app.py` - Main Flask application
- ✅ `requirements.txt` - Python dependencies
- ✅ `templates/index.html` - HTML form (moved from root)
- ✅ `templates/success.html` - Success page

---

## Installation & Setup

### Step 1: Install Dependencies

```bash
cd /Users/sneha/Desktop/python-code/my_project/employee-form
pip3 install -r requirements.txt
```

This installs:
- Flask - Web framework
- Flask-SQLAlchemy - Database ORM
- Werkzeug - WSGI utilities

### Step 2: Run the Application

```bash
python3 app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Running on http://0.0.0.0:5000
```

### Step 3: Open in Browser

Open: http://localhost:5000/

---

## What's Working Now

✅ **Form Display** - The form loads correctly
✅ **Form Submission** - Form data is received by Flask
✅ **Success Page** - Redirects to success page after submission
⚠️ **Database** - Not yet implemented (Step 5)
⚠️ **Email** - Not yet implemented (Step 8)

---

## Testing

1. Start the Flask app: `python3 app.py`
2. Open: http://localhost:5000/
3. Fill out the form
4. Click "Submit Application"
5. You should see the success page

**Check Terminal:**
- Form data will be printed in the terminal (for testing)

---

## Next Steps

- ⏭️ **Step 5**: Setup Database (SQLAlchemy)
- ⏭️ **Step 6**: Store Form Data in Database
- ⏭️ **Step 7**: Show Submission Notification
- ⏭️ **Step 8**: Send Confirmation Email (reference only)

---

## Troubleshooting

### If you get "ModuleNotFoundError":
```bash
pip3 install -r requirements.txt
```

### If port 5000 is in use:
Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Use different port
```

### If you get import errors:
Make sure you're in the correct directory:
```bash
cd /Users/sneha/Desktop/python-code/my_project/employee-form
```
