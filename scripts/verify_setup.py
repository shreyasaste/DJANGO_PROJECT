#!/usr/bin/env python3
"""
Verification script to check if everything is set up correctly
"""

import os
import sys

print("=" * 60)
print("SETUP VERIFICATION")
print("=" * 60)
print()

# Check 1: Virtual environment
print("1. Checking Virtual Environment...")
if os.path.exists('venv'):
    print("   ✓ Virtual environment exists")
else:
    print("   ✗ Virtual environment NOT found")
    sys.exit(1)

# Check 2: Dependencies
print("\n2. Checking Dependencies...")
try:
    import django
    print(f"   ✓ Django {django.get_version()} installed")
except ImportError:
    print("   ✗ Django NOT installed")
    sys.exit(1)

try:
    import psycopg2
    print("   ✓ psycopg2 installed")
except ImportError:
    print("   ✗ psycopg2 NOT installed")
    sys.exit(1)

try:
    import corsheaders
    print("   ✓ django-cors-headers installed")
except ImportError:
    print("   ✗ django-cors-headers NOT installed")
    sys.exit(1)

# Check 3: Django setup
print("\n3. Checking Django Configuration...")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_backend.settings')
try:
    django.setup()
    print("   ✓ Django configured correctly")
except Exception as e:
    print(f"   ✗ Django configuration error: {e}")
    sys.exit(1)

# Check 4: Database connection
print("\n4. Checking Database Connection...")
try:
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()[0]
    print(f"   ✓ PostgreSQL connected")
    print(f"   ✓ Version: {version[:50]}...")
except Exception as e:
    print(f"   ✗ Database connection failed: {e}")
    sys.exit(1)

# Check 5: Tables
print("\n5. Checking Database Tables...")
try:
    cursor.execute("""
        SELECT COUNT(*) 
        FROM information_schema.tables 
        WHERE table_schema='public' 
        AND table_name LIKE 'attendance_%'
    """)
    count = cursor.fetchone()[0]
    print(f"   ✓ Found {count} attendance tables")
except Exception as e:
    print(f"   ✗ Error checking tables: {e}")

# Check 6: Models
print("\n6. Checking Models...")
try:
    from attendance.models import Subject, Lecture, AttendanceRecord, UserSetting
    from django.contrib.auth.models import User
    
    print(f"   ✓ Users: {User.objects.count()}")
    print(f"   ✓ Subjects: {Subject.objects.count()}")
    print(f"   ✓ Lectures: {Lecture.objects.count()}")
    print(f"   ✓ Records: {AttendanceRecord.objects.count()}")
except Exception as e:
    print(f"   ✗ Error checking models: {e}")

# Check 7: Files
print("\n7. Checking Files...")
files_to_check = [
    'index2.html',
    'index2_backup.html',
    'test_api.html',
    'attendance/static/attendance/app-api.js',
    'attendance/static/attendance/storage-adapter.js',
]

for file in files_to_check:
    if os.path.exists(file):
        print(f"   ✓ {file}")
    else:
        print(f"   ✗ {file} NOT found")

# Check 8: Server
print("\n8. Checking Server...")
try:
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 8000))
    if result == 0:
        print("   ✓ Server is running on port 8000")
    else:
        print("   ⚠ Server is NOT running")
        print("   Run: python manage.py runserver")
    sock.close()
except Exception as e:
    print(f"   ⚠ Could not check server: {e}")

print("\n" + "=" * 60)
print("VERIFICATION COMPLETE!")
print("=" * 60)
print("\nYour setup is ready!")
print("\nNext steps:")
print("1. Make sure server is running: python manage.py runserver")
print("2. Open browser: http://127.0.0.1:8000/index2.html")
print("3. Register and start using the app!")
print("\n" + "=" * 60)
