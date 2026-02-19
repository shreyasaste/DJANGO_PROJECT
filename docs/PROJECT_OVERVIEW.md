# Project Overview

## What This Application Does

This is an attendance tracking web application where users can:
- Create and manage subjects/courses
- Schedule lectures
- Mark attendance (present/absent/off)
- View attendance statistics and calendar
- Track attendance patterns over time

## How to Use

1. **Start the server:** Double-click `START_SERVER.bat` in the root folder
2. **Open the app:** Go to http://127.0.0.1:8000/index2.html
3. **Register:** Create a new account (first time users)
4. **Login:** Use your credentials to access your data
5. **Add subjects:** Create subjects you want to track
6. **Mark attendance:** Click on dates to mark present/absent/off

## Folder Structure

- `attendance/` - Main Django app with models, views, and frontend files
- `attendance_backend/` - Django project settings and configuration
- `backups/` - Old HTML files and test pages (safe to ignore)
- `docs/` - Documentation and setup guides
- `scripts/` - Utility scripts for database checking and testing
- `venv/` - Python virtual environment (don't modify)

## Key Files

- `index2.html` - Main application frontend
- `manage.py` - Django management commands
- `requirements.txt` - Python dependencies
- `START_SERVER.bat` - Quick start script
- `README.md` - Detailed technical documentation

## Database

- Uses PostgreSQL database named `attendance_manager`
- Each user's data is completely separate
- Authentication data stored securely
- All changes saved automatically

## Need Help?

- Check `README.md` for technical details
- Check `docs/` folder for setup guides
- Clear browser cache (Ctrl+Shift+R) if you see visual issues
- Make sure server is running before accessing the app
