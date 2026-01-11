# How to Test the HTML Form

## Method 1: Direct Browser Open (Easiest - Recommended)

1. Navigate to the folder:
   ```
   /Users/sneha/Desktop/python-code/my_project/employee-form/
   ```

2. **Double-click** `index.html`
   - OR right-click → Open With → Browser (Chrome/Safari/Firefox)

3. The form will open directly in your browser - **No server needed!**

---

## Method 2: Using Python HTTP Server

### Step 1: Open Terminal

### Step 2: Navigate to the folder:
```bash
cd /Users/sneha/Desktop/python-code/my_project/employee-form
```

### Step 3: Start the server:
```bash
python3 -m http.server 8000
```

You should see:
```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

### Step 4: Open in browser:
Open one of these URLs:
- http://localhost:8000/
- http://localhost:8000/index.html
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/index.html

### Step 5: Stop the server:
- Press `Ctrl + C` in the terminal when done

---

## Troubleshooting

### If you get 404 error:

1. **Make sure you're in the right directory:**
   ```bash
   pwd
   # Should show: /Users/sneha/Desktop/python-code/my_project/employee-form
   ```

2. **Check if index.html exists:**
   ```bash
   ls -la index.html
   # Should show the file
   ```

3. **Try accessing just the root URL:**
   - Use: http://localhost:8000/ (without index.html)
   - Python server automatically serves index.html from root

4. **Check if port 8000 is already in use:**
   ```bash
   lsof -i :8000
   # If something is using it, use a different port:
   python3 -m http.server 8080
   ```

---

## What You Should See

When the form loads correctly, you should see:
- ✅ A centered form with a white background
- ✅ "Job Application Form" heading
- ✅ Bootstrap-styled form fields
- ✅ All input fields (First Name, Last Name, Email, Date, Occupation)
- ✅ A blue "Submit Application" button

---

## Notes

- **Method 1 is simpler** - just double-click the HTML file
- **Method 2 is useful** when you add Flask backend later
- The form won't submit yet (no backend) - we'll add that next!



Here’s how to test everything:

## Testing guide

### Step 1: Install new dependencies

```bash
cd /Users/sneha/Desktop/python-code/my_project/employee-form
pip3 install -r requirements.txt
```

This installs:
- Flask-WTF (form validation)
- WTForms (form fields)
- python-dotenv (environment variables)

---

### Step 2: Create .env file (optional)

```bash
cp .env.example .env
```

Then edit `.env` and change:
- `SECRET_KEY` - Use a random string
- `ADMIN_PASSWORD` - Change from default `admin123`

If you skip this, it uses default values.

---

### Step 3: Run the Flask app

```bash
python3 app.py
```

You should see:
```
Database initialized!
 * Running on http://127.0.0.1:5000
```

---

## What to test

### Test 1: Form validation

1. Open: http://localhost:5000/
2. Try submitting empty form → Should show error messages
3. Try invalid email (e.g., "test") → Should show email error
4. Try short name (e.g., "A") → Should show length error
5. Try past date → Should show date error
6. Fill correctly → Should submit successfully

What to check:
- Error messages appear for each field
- Form doesn't submit with invalid data
- Success message appears when valid

---

### Test 2: Database storage

1. Submit a valid form
2. Check terminal → Should print "Application Saved"
3. Check folder → Should see `instance/data.db` file created
4. Submit another form with different email
5. Run: `python3 view_applications.py` → Should show all applications

What to check:
- Database file created
- Data saved correctly
- Multiple applications stored
- `view_applications.py` shows all data

---

### Test 3: Duplicate email protection

1. Submit form with email: `test@example.com`
2. Try submitting again with same email
3. Should see: "This email has already been used" warning

What to check:
- Duplicate email is rejected
- Warning message appears
- Form doesn't save duplicate

---

### Test 4: Admin panel

1. Open: http://localhost:5000/admin
2. Should see login page (no password entered)
3. Enter password: `admin123` (or your custom password)
4. Click "Login"
5. Should see all applications in a table

What to check:
- Login page appears without password
- Admin panel shows after correct password
- All applications displayed
- Table shows: ID, Name, Email, Date, Occupation, Submitted date

---

### Test 5: Delete application (admin)

1. In admin panel, click "Delete" on any application
2. Confirm deletion
3. Application should be removed
4. Table should update

What to check:
- Delete button works
- Confirmation dialog appears
- Application removed from database
- Table updates immediately

---

### Test 6: API endpoint

1. Open: http://localhost:5000/api/applications
2. Should see JSON data with all applications

What to check:
- JSON format is valid
- All applications included
- Has `success`, `count`, and `applications` fields
- Can be used by other applications

---

### Test 7: Error pages

1. Open: http://localhost:5000/nonexistent-page
2. Should see custom 404 error page

What to check:
- Custom 404 page appears
- Shows "Page not found" message
- Has link back to home

---

### Test 8: Flash messages

1. Submit form successfully → Success message appears
2. Try duplicate email → Warning message appears
3. Try invalid data → Error messages appear

What to check:
- Messages appear at top of form
- Messages are color-coded (green=success, red=error, yellow=warning)
- Messages can be dismissed (X button)

---

## Quick test checklist

- [ ] Form validation works (errors show for invalid data)
- [ ] Valid form submits successfully
- [ ] Database file created (`instance/data.db`)
- [ ] Data saved correctly (check terminal output)
- [ ] Duplicate email rejected
- [ ] Admin panel accessible with password
- [ ] Can view all applications in admin
- [ ] Can delete applications
- [ ] API endpoint returns JSON
- [ ] Error pages work (404)
- [ ] Flash messages appear correctly

---

## Testing commands summary

```bash
# 1. Install dependencies
pip3 install -r requirements.txt

# 2. Run app
python3 app.py

# 3. In another terminal - View applications
python3 view_applications.py
```

---

## URLs to test

- Form: http://localhost:5000/
- Admin: http://localhost:5000/admin?password=admin123
- API: http://localhost:5000/api/applications
- 404 Test: http://localhost:5000/nonexistent

---

## Expected results

- Form validates all fields
- Data saves to database
- Admin panel shows all applications
- API returns JSON data
- Error handling works
- Flash messages display correctly

Start with Step 1 (install dependencies), then test each feature. If anything doesn't work, share the error or behavior you see.
