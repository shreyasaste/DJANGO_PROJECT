# How to Delete User Data

## Overview
There are multiple ways to delete a user's data from the Attendance Manager system. Choose the method that best fits your needs.

---

## Method 1: Using Django Admin Panel (Recommended for Teachers/Admins)

### Step 1: Create Admin Account (One-time setup)

1. Open PowerShell in the project directory
2. Activate virtual environment:
   ```powershell
   cd "C:\Users\shreya\OneDrive\Desktop\DJANGO_PROJECT\django(@)\django(2)"
   .\venv\Scripts\Activate.ps1
   ```

3. Create superuser:
   ```powershell
   python manage.py createsuperuser
   ```

4. Enter details when prompted:
   ```
   Username: admin
   Email: admin@example.com
   Password: [your secure password]
   Password (again): [same password]
   ```

### Step 2: Access Admin Panel

1. Make sure server is running:
   ```powershell
   python manage.py runserver
   ```

2. Open browser and go to:
   ```
   http://127.0.0.1:8000/admin/
   ```

3. Login with your superuser credentials

### Step 3: Delete User Data

**Option A: Delete Entire User Account**
1. Click on "Users" in the admin panel
2. Find the user you want to delete
3. Check the checkbox next to their name
4. Select "Delete selected users" from the dropdown
5. Click "Go"
6. Confirm deletion

This will automatically delete:
- User account
- All their subjects
- All their lectures
- All their attendance records
- All their settings

**Option B: Delete Only User's Data (Keep Account)**
1. Click on "Subjects" → Find and delete user's subjects
2. Click on "Lectures" → Find and delete user's lectures
3. Click on "Attendance records" → Find and delete user's records
4. Click on "User settings" → Find and delete user's settings

---

## Method 2: Using Python Script (For Developers)

### Create Delete User Script

I'll create a script for you: `scripts/delete_user.py`

### Usage:

1. Activate venv:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. Run the script:
   ```powershell
   python scripts\delete_user.py
   ```

3. Follow the prompts:
   - Enter user's email
   - Confirm deletion

---

## Method 3: Using PostgreSQL pgAdmin (For Database Admins)

### Step 1: Open pgAdmin

1. Open pgAdmin 4
2. Connect to your PostgreSQL server
3. Navigate to: Servers → PostgreSQL → Databases → attendance_manager

### Step 2: Find User ID

1. Right-click on "attendance_manager" → Query Tool
2. Run this query to find the user:
   ```sql
   SELECT id, username, email, first_name 
   FROM auth_user 
   WHERE email = 'user@example.com';
   ```
3. Note the user's `id`

### Step 3: Delete User Data

Run these queries in order (replace `USER_ID` with actual ID):

```sql
-- Delete attendance records
DELETE FROM attendance_attendancerecord WHERE user_id = USER_ID;

-- Delete lectures
DELETE FROM attendance_lecture WHERE user_id = USER_ID;

-- Delete subjects
DELETE FROM attendance_subject WHERE user_id = USER_ID;

-- Delete user settings
DELETE FROM attendance_usersetting WHERE user_id = USER_ID;

-- Delete user account
DELETE FROM auth_user WHERE id = USER_ID;
```

---

## Method 4: Using "Reset App Data" Button (For Users)

### For Users to Delete Their Own Data:

1. Login to the app
2. Go to Settings page
3. Click "Reset App Data" button
4. Confirm deletion

This will:
- Delete all their subjects
- Delete all their lectures
- Delete all their attendance records
- Delete their settings
- Log them out
- Keep their account (can login again with empty data)

---

## Method 5: Using Django Shell (For Developers)

### Step 1: Open Django Shell

```powershell
.\venv\Scripts\Activate.ps1
python manage.py shell
```

### Step 2: Delete User

```python
from django.contrib.auth.models import User
from attendance.models import Subject, Lecture, AttendanceRecord, UserSetting

# Find user by email
user = User.objects.get(email='user@example.com')

# Delete all related data (automatic with CASCADE)
user.delete()

# Or delete only data, keep account
Subject.objects.filter(user=user).delete()
Lecture.objects.filter(user=user).delete()
AttendanceRecord.objects.filter(user=user).delete()
UserSetting.objects.filter(user=user).delete()
```

---

## Comparison of Methods

| Method | Best For | Difficulty | Deletes Account | Requires Admin |
|--------|----------|------------|-----------------|----------------|
| Django Admin | Teachers/Admins | Easy | Yes/No (choice) | Yes |
| Python Script | Batch operations | Medium | Yes/No (choice) | No |
| pgAdmin | Database admins | Medium | Yes | Yes |
| Reset Button | Users themselves | Very Easy | No | No |
| Django Shell | Developers | Hard | Yes/No (choice) | No |

---

## Important Notes

### Data Deletion is Permanent!
- Once deleted, data cannot be recovered
- Always confirm before deleting
- Consider backing up data first

### Cascade Deletion
The database is configured with CASCADE delete, meaning:
- Deleting a user automatically deletes all their data
- Deleting a subject automatically deletes related lectures and attendance
- This prevents orphaned data

### Backup Before Deletion

To backup before deleting:

```powershell
# Backup entire database
pg_dump -U postgres attendance_manager > backup_$(date +%Y%m%d).sql

# Or use pgAdmin: Right-click database → Backup
```

---

## Recommended Approach for Teachers

**Best Practice:**
1. Set up Django Admin panel (one-time)
2. Use admin panel to manage users
3. Can view all data before deleting
4. Can selectively delete data or entire accounts
5. Has confirmation prompts to prevent accidents

---

## Troubleshooting

### "User not found"
- Check email spelling
- User might already be deleted
- Check in admin panel or database

### "Permission denied"
- Need superuser access for admin panel
- Need database credentials for pgAdmin
- Regular users can only delete their own data

### "Foreign key constraint error"
- Shouldn't happen with CASCADE delete
- If it does, delete related data first (subjects, lectures, records)
- Then delete user account

---

## Need Help?

If you need to delete multiple users or have special requirements, you can:
1. Use the Python script (I'll create it for you)
2. Use Django admin panel with bulk actions
3. Write a custom SQL query in pgAdmin
