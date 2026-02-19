# How to Run the Project

## Step-by-Step Instructions

### Step 1: Open PowerShell or CMD

Right-click in the project folder and select:
- "Open in Terminal" or
- "Open PowerShell window here"

### Step 2: Navigate to Project Directory

```powershell
cd "C:\Users\shreya\OneDrive\Desktop\DJANGO_PROJECT\django(@)\django(2)"
```

### Step 3: Activate Virtual Environment

**In PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**In CMD:**
```cmd
venv\Scripts\activate.bat
```

**You should see `(venv)` appear at the start of your command line.**

Example:
```
(venv) PS C:\Users\shreya\OneDrive\Desktop\DJANGO_PROJECT\django(@)\django(2)>
```

### Step 4: Run the Django Server

```powershell
python manage.py runserver
```

You should see output like:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Step 5: Open the Application

Open your web browser and go to:
```
http://127.0.0.1:8000/index2.html
```

### Step 6: Use the Application

- Register a new account (first time)
- Login with your credentials
- Start tracking attendance!

## Quick Method (Using Batch File)

Simply double-click `START_SERVER.bat` in the project folder!

## Stopping the Server

Press `Ctrl + C` in the terminal where the server is running.

## Deactivating Virtual Environment

When you're done, type:
```
deactivate
```

## Troubleshooting

### PowerShell Execution Policy Error

If you get an error like "cannot be loaded because running scripts is disabled", run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### "venv not found" Error

Make sure you're in the correct directory:
```powershell
cd "C:\Users\shreya\OneDrive\Desktop\DJANGO_PROJECT\django(@)\django(2)"
```

### Port Already in Use

If port 8000 is already in use, either:
1. Stop the other server running on port 8000
2. Use a different port: `python manage.py runserver 8001`

### Database Connection Error

1. Make sure PostgreSQL is running
2. Check database credentials in `attendance_backend/settings.py`
3. Verify database `attendance_manager` exists

## Common Commands (with venv activated)

```powershell
# Check if server works
python manage.py check

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# View database tables
python scripts\list_tables.py

# View all data
python scripts\show_all_data.py
```

## Remember

- Always activate venv before running Python commands
- Keep the server running while using the application
- Clear browser cache (Ctrl+Shift+R) if you see visual issues
- Each user's data is completely separate
