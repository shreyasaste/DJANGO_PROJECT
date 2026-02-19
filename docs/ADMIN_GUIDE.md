# Admin Guide - Attendance Manager

## For Teachers and System Administrators

This guide explains how to manage users and data in the Attendance Manager system.

---

## Quick Start for Admins

### 1. Create Admin Account (One-time Setup)

Open PowerShell and run:

```powershell
cd "C:\Users\shreya\OneDrive\Desktop\DJANGO_PROJECT\django(@)\django(2)"
.\venv\Scripts\Activate.ps1
python manage.py createsuperuser
```

Enter your admin credentials:
- Username: `admin` (or your choice)
- Email: `admin@example.com`
- Password: (choose a secure password)

### 2. Access Admin Panel

1. Start the server: `python manage.py runserver`
2. Open browser: http://127.0.0.1:8000/admin/
3. Login with your admin credentials

---

## Common Admin Tasks

### View All Users

**Method 1: Using Script (Easiest)**
```powershell
# Double-click this file:
DELETE_USER.bat

# Or run manually:
.\venv\Scripts\Activate.ps1
python scripts\view_users.py
```

**Method 2: Using Admin Panel**
1. Go to http://127.0.0.1:8000/admin/
2. Click "Users"
3. See list of all users with details

### Delete a User

**Method 1: Using Script (Recommended)**
```powershell
# Double-click this file:
DELETE_USER.bat

# Follow the prompts:
# 1. Select deletion method (by email or ID)
# 2. Choose what to delete (data only or account + data)
# 3. Confirm deletion
```

**Method 2: Using Admin Panel**
1. Go to http://127.0.0.1:8000/admin/
2. Click "Users"
3. Find the user
4. Check the checkbox next to their name
5. Select "Delete selected users" from dropdown
6. Click "Go"
7. Confirm deletion

### View User's Data

**Using Admin Panel:**
1. Login to admin panel
2. Click on "Subjects" to see all subjects
3. Click on "Lectures" to see all lectures
4. Click on "Attendance records" to see all attendance
5. Use filters to find specific user's data

**Using Script:**
```powershell
python scripts\view_users.py
```

This shows:
- All users
- Their subjects
- Their attendance statistics
- Overall attendance percentage

### Reset User's Data (Keep Account)

**Using Script:**
```powershell
python scripts\delete_user.py
# Choose option 1: "Delete only data (keep account)"
```

This will:
- Delete all subjects
- Delete all lectures
- Delete all attendance records
- Keep the user account
- User can login again with empty data

---

## Managing Multiple Users

### Bulk Delete Users

**Using Admin Panel:**
1. Go to Users page
2. Check multiple users
3. Select "Delete selected users"
4. Confirm

**Using Django Shell:**
```powershell
python manage.py shell
```

```python
from django.contrib.auth.models import User

# Delete all users except admin
User.objects.exclude(is_superuser=True).delete()

# Delete users by email domain
User.objects.filter(email__endswith='@student.com').delete()

# Delete inactive users
User.objects.filter(last_login__isnull=True).delete()
```

---

## Database Backup and Restore

### Backup Database

**Before deleting any data, always backup!**

**Method 1: Using pgAdmin**
1. Open pgAdmin
2. Right-click on "attendance_manager" database
3. Select "Backup..."
4. Choose location and filename
5. Click "Backup"

**Method 2: Using Command Line**
```powershell
pg_dump -U postgres attendance_manager > backup_20260219.sql
```

### Restore Database

```powershell
psql -U postgres attendance_manager < backup_20260219.sql
```

---

## User Data Structure

Each user has:

### 1. User Account (auth_user table)
- Username
- Email
- Password (hashed)
- Name
- Join date
- Last login

### 2. Subjects (attendance_subject table)
- Subject name
- Subject code
- User ID (foreign key)

### 3. Lectures (attendance_lecture table)
- Subject ID (foreign key)
- Day of week
- Time
- User ID (foreign key)

### 4. Attendance Records (attendance_attendancerecord table)
- Subject ID (foreign key)
- Date
- Status (present/absent/off)
- Lecture time
- User ID (foreign key)

### 5. User Settings (attendance_usersetting table)
- Target percentage
- User ID (foreign key)

**Note:** All data is linked to user via foreign keys with CASCADE delete, so deleting a user automatically deletes all their data.

---

## Security Best Practices

### 1. Admin Account Security
- Use strong password
- Don't share admin credentials
- Change password regularly
- Use unique username (not "admin")

### 2. User Management
- Regularly review user accounts
- Delete inactive accounts
- Monitor for suspicious activity
- Keep backups before bulk operations

### 3. Database Security
- Keep PostgreSQL password secure
- Don't expose database to internet
- Regular backups
- Test restore process

---

## Troubleshooting

### Can't Access Admin Panel

**Problem:** "Page not found" or "Login failed"

**Solutions:**
1. Ensure server is running: `python manage.py runserver`
2. Check URL: http://127.0.0.1:8000/admin/ (note the trailing slash)
3. Verify superuser exists: `python manage.py createsuperuser`
4. Check credentials are correct

### Can't Delete User

**Problem:** "Foreign key constraint" error

**Solution:**
- This shouldn't happen with CASCADE delete
- If it does, delete related data first:
  1. Delete user's attendance records
  2. Delete user's lectures
  3. Delete user's subjects
  4. Delete user's settings
  5. Then delete user account

### Script Not Working

**Problem:** "Module not found" or "Django not setup"

**Solutions:**
1. Ensure venv is activated: `.\venv\Scripts\Activate.ps1`
2. Check you're in correct directory
3. Verify Django is installed: `pip list | findstr Django`
4. Run from project root directory

---

## Advanced Operations

### Export User Data

```python
# In Django shell
from django.contrib.auth.models import User
from attendance.models import Subject, AttendanceRecord
import json

user = User.objects.get(email='user@example.com')
subjects = Subject.objects.filter(user=user)
records = AttendanceRecord.objects.filter(user=user)

data = {
    'user': {
        'email': user.email,
        'name': user.first_name,
    },
    'subjects': [{'name': s.name, 'code': s.code} for s in subjects],
    'records': [{'date': str(r.date), 'status': r.status} for r in records]
}

with open('user_data.json', 'w') as f:
    json.dump(data, f, indent=2)
```

### Transfer Data Between Users

```python
# In Django shell
from django.contrib.auth.models import User
from attendance.models import Subject

old_user = User.objects.get(email='old@example.com')
new_user = User.objects.get(email='new@example.com')

# Transfer all subjects
Subject.objects.filter(user=old_user).update(user=new_user)
```

### Generate User Report

```python
# In Django shell
from django.contrib.auth.models import User
from attendance.models import AttendanceRecord

for user in User.objects.all():
    records = AttendanceRecord.objects.filter(user=user)
    present = records.filter(status='present').count()
    absent = records.filter(status='absent').count()
    total = present + absent
    pct = (present / total * 100) if total > 0 else 0
    
    print(f"{user.email}: {pct:.1f}% ({present}P/{absent}A)")
```

---

## Quick Reference Commands

```powershell
# View all users
python scripts\view_users.py

# Delete user (interactive)
python scripts\delete_user.py

# Create admin account
python manage.py createsuperuser

# Open Django shell
python manage.py shell

# Backup database
pg_dump -U postgres attendance_manager > backup.sql

# Restore database
psql -U postgres attendance_manager < backup.sql

# View database tables
python scripts\list_tables.py

# View all data
python scripts\show_all_data.py
```

---

## Support

For more help:
- See `HOW_TO_DELETE_USER_DATA.md` for detailed deletion instructions
- See `README.md` for technical documentation
- See `QUICK_REFERENCE.md` for common commands
