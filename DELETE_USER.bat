@echo off
echo ========================================
echo Delete User Data - Attendance Manager
echo ========================================
echo.

cd /d "%~dp0"

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Running delete user script...
echo.

python scripts\delete_user.py

echo.
echo ========================================
echo.
pause
