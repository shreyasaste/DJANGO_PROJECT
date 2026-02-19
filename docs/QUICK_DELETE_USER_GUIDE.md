# Quick Guide: How to Delete a User

## 🎯 Easiest Method (For Teachers/Admins)

### Step 1: Double-click `DELETE_USER.bat`

### Step 2: Follow the prompts

```
========================================
Delete User Data - Attendance Manager
========================================

ALL USERS IN SYSTEM
============================================================
ID    Username             Email                          Name
------------------------------------------------------------
1     admin               admin@example.com              Admin
2     john                john@student.com               John Doe
3     jane                jane@student.com               Jane Smith
============================================================

📝 Select deletion method:
   1. Delete by Email
   2. Delete by User ID
   3. Cancel

Enter choice (1-3): 1

📧 Enter user email: john@student.com

👤 User Found:
   ID: 2
   Username: john
   Email: john@student.com
   Name: John Doe

🗑️  What do you want to delete?
   1. Delete only data (keep account)
   2. Delete account and all data
   3. Cancel

Enter choice (1-3): 2

📊 User Data Summary:
   - Subjects: 4
   - Lectures: 12
   - Attendance Records: 45

⚠️  WARNING: This will permanently delete:
   - User account: john@student.com
   - All user data (subjects, lectures, attendance)
   - User will NOT be able to login anymore

⚠️  Are you absolutely sure? Type 'DELETE' to confirm: DELETE

✅ Successfully deleted user account and all data:
   Username: john
   Email: john@student.com
```

---

## 🔧 Alternative Methods

### Method 1: Django Admin Panel

1. **Setup (one-time):**
   ```powershell
   .\venv\Scripts\Activate.ps1
   python manage.py createsuperuser
   ```

2. **Access:**
   - Go to: http://127.0.0.1:8000/admin/
   - Login with admin credentials

3. **Delete:**
   - Click "Users"
   - Find user
   - Check checkbox
   - Select "Delete selected users"
   - Confirm

### Method 2: View Users First

```powershell
# Double-click DELETE_USER.bat
# Or run:
.\venv\Scripts\Activate.ps1
python scripts\view_users.py
```

This shows all users and their data before deleting.

---

## 📋 What Gets Deleted?

### Option 1: Delete Only Data (Keep Account)
- ✅ All subjects deleted
- ✅ All lectures deleted
- ✅ All attendance records deleted
- ✅ All settings deleted
- ❌ Account remains (user can login with empty data)

### Option 2: Delete Account and Data
- ✅ User account deleted
- ✅ All subjects deleted
- ✅ All lectures deleted
- ✅ All attendance records deleted
- ✅ All settings deleted
- ❌ User cannot login anymore

---

## ⚠️ Important Notes

### Before Deleting:
- ✅ Backup database (if needed)
- ✅ Confirm correct user
- ✅ Understand deletion is permanent

### After Deleting:
- ✅ Data cannot be recovered
- ✅ User will need to re-register (if account deleted)
- ✅ Other users' data is not affected

---

## 🆘 Need Help?

### Detailed Guides:
- `docs/HOW_TO_DELETE_USER_DATA.md` - Complete deletion guide
- `docs/ADMIN_GUIDE.md` - Admin panel and management
- `README.md` - Technical documentation

### Quick Commands:
```powershell
# View all users
python scripts\view_users.py

# Delete user (interactive)
python scripts\delete_user.py

# Access admin panel
# http://127.0.0.1:8000/admin/
```

---

## 🎓 For Teachers

**Recommended Workflow:**

1. **View all students:**
   ```
   python scripts\view_users.py
   ```

2. **Identify user to delete:**
   - Note their email or ID

3. **Delete user:**
   ```
   python scripts\delete_user.py
   ```

4. **Verify deletion:**
   ```
   python scripts\view_users.py
   ```

**Best Practice:**
- Use Django Admin panel for regular management
- Use scripts for quick operations
- Always backup before bulk deletions
