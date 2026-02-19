# 🚀 START HERE - Attendance Manager

Welcome! This is your attendance tracking application.

## ⚡ Quick Start (Easiest Way)

1. **Double-click** `START_SERVER.bat`
2. **Open browser** to: http://127.0.0.1:8000/index2.html
3. **Register** or **Login**
4. **Start tracking attendance!**

## 📖 Need More Help?

- **First time user?** Read `HOW_TO_RUN.md`
- **Want to understand the project?** Read `PROJECT_OVERVIEW.md`
- **Need commands reference?** Read `QUICK_REFERENCE.md`
- **Technical details?** Read `README.md`

## 🔧 Manual Start (PowerShell)

```powershell
# 1. Navigate to project
cd "C:\Users\shreya\OneDrive\Desktop\DJANGO_PROJECT\django(@)\django(2)"

# 2. Activate venv
.\venv\Scripts\Activate.ps1

# 3. Run server
python manage.py runserver
```

## 📁 Project Structure

```
django(2)/
├── attendance/          # Main app (models, views, frontend)
├── attendance_backend/  # Django settings
├── backups/            # Old files (ignore)
├── docs/               # Documentation
├── scripts/            # Utility scripts
├── venv/               # Virtual environment
├── index2.html         # Main application
├── manage.py           # Django management
└── START_SERVER.bat    # Quick start
```

## ✅ What This App Does

- Track attendance for multiple subjects
- Mark present/absent/off for each lecture
- View attendance calendar with color coding
- See attendance statistics
- Multi-user support (each user has separate data)

## 🔑 Important Notes

- **Always activate venv** before running Python commands
- **Clear browser cache** (Ctrl+Shift+R) if you see issues
- **Each user's data is separate** - login to see your data
- **Database:** PostgreSQL (attendance_manager)
- **Server:** http://127.0.0.1:8000/

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Server won't start | Activate venv first |
| Visual issues | Clear browser cache (Ctrl+Shift+R) |
| Old data showing | Logout and login again |
| Database error | Check PostgreSQL is running |

## 📚 Documentation Files

- `START_HERE.md` ← You are here!
- `HOW_TO_RUN.md` - Step-by-step running instructions
- `PROJECT_OVERVIEW.md` - Simple project overview
- `QUICK_REFERENCE.md` - Common commands and tips
- `README.md` - Complete technical documentation

## 🎯 Next Steps

1. Start the server (use START_SERVER.bat)
2. Open http://127.0.0.1:8000/index2.html
3. Register a new account
4. Add your subjects
5. Start marking attendance!

---

**Need help?** Check the `docs/` folder for more guides!
