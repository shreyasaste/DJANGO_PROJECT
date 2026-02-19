import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_backend.settings')
django.setup()

from django.db import connection

cursor = connection.cursor()
cursor.execute("""
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema='public' 
    AND table_name LIKE 'attendance_%'
    ORDER BY table_name
""")

tables = cursor.fetchall()
print("=" * 50)
print("TABLES IN DATABASE:")
print("=" * 50)
for table in tables:
    print(f"✓ {table[0]}")
    
print("\n" + "=" * 50)
print(f"Total: {len(tables)} attendance tables found")
print("=" * 50)

# Check if there's any data
from attendance.models import Subject, Lecture, AttendanceRecord
from django.contrib.auth.models import User

print(f"\nUsers: {User.objects.count()}")
print(f"Subjects: {Subject.objects.count()}")
print(f"Lectures: {Lecture.objects.count()}")
print(f"Records: {AttendanceRecord.objects.count()}")
