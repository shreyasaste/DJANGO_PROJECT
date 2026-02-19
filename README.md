# Attendance Manager

A web-based attendance tracking application with Django backend and PostgreSQL database.

---

## 🚀 Quick Start

### Start the Server
```
Double-click: START_SERVER.bat
```

### Open the App
```
http://127.0.0.1:8000/index2.html
```

### First Time Setup
1. Register a new account
2. Add your subjects
3. Add lectures to timetable
4. Start marking attendance!

---

## 📋 Features

- ✅ User authentication (register/login/logout)
- ✅ Multi-user support (each user's data is separate)
- ✅ Subject management
- ✅ Lecture scheduling
- ✅ Attendance tracking (present/absent/off)
- ✅ Visual calendar with color-coded attendance
- ✅ Attendance statistics and analytics
- ✅ Customizable attendance target

---

## 🗂️ Project Structure

```
django(2)/
├── attendance/              # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # API endpoints
│   ├── static/             # Frontend JavaScript & CSS
│   └── templates/          # HTML templates
├── attendance_backend/      # Django settings
├── backups/                # Backup files
├── docs/                   # Documentation
├── scripts/                # Utility scripts
├── venv/                   # Virtual environment
├── index2.html             # Main application
├── manage.py               # Django management
├── requirements.txt        # Python dependencies
├── START_SERVER.bat        # Quick start script
├── DELETE_USER.bat         # Delete user script
└── README.md               # This file
```

---

## 💾 Database

- **Type:** PostgreSQL
- **Name:** attendance_manager
- **User:** postgres
- **Password:** 87654321
- **Host:** localhost
- **Port:** 5432

### Tables:
- `auth_user` - User accounts
- `attendance_subject` - Subjects/courses
- `attendance_lecture` - Lectures
- `attendance_attendancerecord` - Attendance records
- `attendance_usersetting` - User preferences

---

## 🔧 Manual Setup

### Activate Virtual Environment

**PowerShell:**
```powershell
cd "C:\Users\shreya\OneDrive\Desktop\DJANGO_PROJECT\django(@)\django(2)"
.\venv\Scripts\Activate.ps1
```

**CMD:**
```cmd
cd C:\Users\shreya\OneDrive\Desktop\DJANGO_PROJECT\django(@)\django(2)
venv\Scripts\activate.bat
```

### Run Server
```powershell
python manage.py runserver
```

### Run Migrations
```powershell
python manage.py migrate
```

---

## 👥 User Management (For Teachers/Admins)

### View All Users
```powershell
python scripts\view_users.py
```

### Delete a User
```powershell
# Easy way:
Double-click DELETE_USER.bat

# Or manually:
python scripts\delete_user.py
```

### Create Admin Account
```powershell
python manage.py createsuperuser
```

### Access Admin Panel
```
http://127.0.0.1:8000/admin/
```

---

## 🛠️ Utility Scripts

Located in `scripts/` folder:

**User Management:**
- `view_users.py` - View all users and statistics
- `delete_user.py` - Delete user data (interactive)

**Database:**
- `check_database.py` - Check database connection
- `list_tables.py` - List all database tables
- `show_all_data.py` - Display all data
- `check_auth_data.py` - View authentication data

**Testing:**
- `create_test_data.py` - Create sample data
- `verify_setup.py` - Verify project setup

---

## 📚 Documentation

All documentation is in the `docs/` folder:

**Getting Started:**
- `HOW_TO_RUN.md` - Detailed running instructions
- `PROJECT_OVERVIEW.md` - Simple project overview

**Admin Guides:**
- `ADMIN_GUIDE.md` - Complete admin guide
- `HOW_TO_DELETE_USER_DATA.md` - User deletion guide
- `QUICK_DELETE_USER_GUIDE.md` - Quick deletion reference

**Technical Fixes:**
- `LOGOUT_FIX.md` - Logout functionality fix
- `DATE_AND_MODAL_FIX.md` - Date and modal fixes
- `CRITERIA_DROPDOWN_FIX.md` - Dropdown styling fix
- `FINAL_FIXES_SUMMARY.md` - All fixes summary

---

## 🎯 Common Tasks

### Mark Attendance
1. Go to "Today" page
2. Click ✔ for Present, ✖ for Absent, ➖ for Off

### Add Subject
1. Click + button
2. Enter subject name and code
3. Click Add

### Add Lecture to Timetable
1. Go to "Timetable" page
2. Click + button
3. Select day, subject, and time

### Change Attendance Target
1. Go to "Settings" page
2. Select target percentage (75%, 80%, 85%, 90%)

### View Calendar
1. Go to "Calendar" page
2. See color-coded attendance
3. Click any date to see details

---

## 🔍 Troubleshooting

### Server Won't Start
- Activate virtual environment first
- Check if PostgreSQL is running
- Verify database credentials in `settings.py`

### Visual Issues (Old Data Showing)
- Clear browser cache: `Ctrl + Shift + R`
- Logout and login again
- Check browser console (F12) for errors

### Database Connection Error
- Ensure PostgreSQL is running
- Check database name: `attendance_manager`
- Verify credentials: user=postgres, password=87654321

### Attendance Not Saving
- Check server is running
- Check browser console for errors
- Verify database connection
- Try logout and login again

---

## 🔐 Security Notes

- Each user's data is completely isolated
- Passwords are hashed and secure
- Session-based authentication
- CSRF protection enabled
- CORS configured for API access

---

## 🌐 Technology Stack

- **Backend:** Django 5.2.11
- **Database:** PostgreSQL (psycopg2-binary 2.9.11)
- **Frontend:** Vanilla JavaScript, HTML5, CSS3
- **CORS:** django-cors-headers 4.9.0

---

## 📞 Support

For detailed help, see documentation in `docs/` folder:
- Setup issues → `docs/HOW_TO_RUN.md`
- User management → `docs/ADMIN_GUIDE.md`
- Technical details → `docs/FINAL_FIXES_SUMMARY.md`

---

## ✅ Project Status

**Complete and Ready to Use!**

All features implemented:
- ✅ Database integration
- ✅ User authentication
- ✅ Attendance tracking
- ✅ Calendar view
- ✅ Statistics
- ✅ Multi-user support
- ✅ Admin tools

---

**Made with ❤️ for Attendance Management**
