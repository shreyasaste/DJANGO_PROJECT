# Quick Reference Guide

## Virtual Environment (venv)

**IMPORTANT:** Always activate the virtual environment before running any Python commands!

**In PowerShell:**
```powershell
cd "C:\Users\shreya\OneDrive\Desktop\DJANGO_PROJECT\django(@)\django(2)"
.\venv\Scripts\Activate.ps1
```

**In CMD:**
```cmd
cd C:\Users\shreya\OneDrive\Desktop\DJANGO_PROJECT\django(@)\django(2)
venv\Scripts\activate.bat
```

**You'll know venv is activated when you see `(venv)` at the start of your command prompt.**

**To deactivate:**
```
deactivate
```

## Starting the Server

**Option 1 (Using Batch File):**
```
Double-click START_SERVER.bat
```

**Option 2 (Manual in PowerShell):**
```powershell
# Navigate to project directory
cd "C:\Users\shreya\OneDrive\Desktop\DJANGO_PROJECT\django(@)\django(2)"

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run server
python manage.py runserver
```

**Option 3 (Manual in CMD):**
```cmd
cd C:\Users\shreya\OneDrive\Desktop\DJANGO_PROJECT\django(@)\django(2)
venv\Scripts\activate.bat
python manage.py runserver
```

## Accessing the Application

- Main App: http://127.0.0.1:8000/index2.html
- Admin Panel: http://127.0.0.1:8000/admin/

## Common Commands

### Database Operations
```powershell
# First, activate venv
.\venv\Scripts\Activate.ps1

# Run migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Check database tables
python scripts\list_tables.py

# View all data
python scripts\show_all_data.py
```

### Testing
```powershell
# Make sure venv is activated first
.\venv\Scripts\Activate.ps1

# Create test data
python scripts\create_test_data.py

# Verify setup
python scripts\verify_setup.py

# Check authentication data
python scripts\check_auth_data.py
```

## Troubleshooting

### Visual Issues (attendance not showing)
1. Clear browser cache: `Ctrl + Shift + R`
2. Check browser console for errors (F12)
3. Verify server is running

### Server Won't Start
1. Check if virtual environment is activated
2. Verify PostgreSQL is running
3. Check database credentials in `attendance_backend/settings.py`

### Database Issues
1. Verify database exists: `attendance_manager`
2. Check PostgreSQL credentials (user: postgres, password: 87654321)
3. Run migrations: `python manage.py migrate`

### Old Data Showing
1. Clear browser cache
2. Logout and login again
3. Check if correct user is logged in

## File Locations

- **Frontend:** `index2.html`
- **API Functions:** `attendance/static/attendance/app-api.js`
- **Storage Adapter:** `attendance/static/attendance/storage-adapter.js`
- **Database Models:** `attendance/models.py`
- **API Views:** `attendance/views.py`
- **Settings:** `attendance_backend/settings.py`

## Database Tables

- `auth_user` - User accounts
- `attendance_subject` - Subjects/courses
- `attendance_lecture` - Lectures
- `attendance_attendancerecord` - Attendance records
- `attendance_usersetting` - User preferences

## API Endpoints

All require authentication (except register/login):

- `POST /api/register/` - Register new user
- `POST /api/login/` - Login
- `POST /api/logout/` - Logout
- `GET/POST /api/subjects/` - Manage subjects
- `GET/POST /api/lectures/` - Manage lectures
- `GET/POST /api/attendance/` - Manage attendance
- `GET/POST /api/settings/` - User settings

## Tips

- Each user's data is completely separate
- Always clear cache after code changes
- Use browser console (F12) to debug JavaScript issues
- Check server terminal for backend errors
- Backup database before major changes
