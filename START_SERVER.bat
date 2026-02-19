@echo off
echo Starting Django Development Server...
echo.
cd /d "%~dp0"
call venv\Scripts\activate
python manage.py runserver
pause
