#!/usr/bin/env python3
"""
Create test data in the database
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_backend.settings')
django.setup()

from django.contrib.auth.models import User
from attendance.models import Subject, Lecture, AttendanceRecord, UserSetting
from datetime import date, time

print("=" * 60)
print("CREATING TEST DATA")
print("=" * 60)

# Create a test user
print("\n1. Creating test user...")
user, created = User.objects.get_or_create(
    username='test@example.com',
    defaults={
        'email': 'test@example.com',
        'first_name': 'Test User'
    }
)
if created:
    user.set_password('test123')
    user.save()
    print(f"   ✓ Created user: {user.username}")
else:
    print(f"   ✓ User already exists: {user.username}")

# Create user setting
print("\n2. Creating user settings...")
setting, created = UserSetting.objects.get_or_create(
    user=user,
    defaults={'target_percentage': 80}
)
print(f"   ✓ Target: {setting.target_percentage}%")

# Create subjects
print("\n3. Creating subjects...")
subjects_data = [
    ('Mathematics', 'MATH101'),
    ('Physics', 'PHY101'),
    ('Chemistry', 'CHEM101'),
    ('Computer Science', 'CS101'),
]

subjects = []
for name, code in subjects_data:
    subject, created = Subject.objects.get_or_create(
        user=user,
        name=name,
        defaults={'code': code}
    )
    subjects.append(subject)
    status = "Created" if created else "Already exists"
    print(f"   ✓ {status}: {name} ({code})")

# Create lectures
print("\n4. Creating timetable...")
lectures_data = [
    (subjects[0], 'monday', time(9, 0)),
    (subjects[1], 'monday', time(11, 0)),
    (subjects[2], 'tuesday', time(10, 0)),
    (subjects[3], 'wednesday', time(14, 0)),
]

for subject, day, lecture_time in lectures_data:
    lecture, created = Lecture.objects.get_or_create(
        user=user,
        subject=subject,
        day=day,
        time=lecture_time
    )
    status = "Created" if created else "Already exists"
    print(f"   ✓ {status}: {subject.name} on {day} at {lecture_time}")

# Create attendance records
print("\n5. Creating attendance records...")
records_data = [
    (subjects[0], date(2026, 2, 17), 'present'),
    (subjects[0], date(2026, 2, 18), 'present'),
    (subjects[1], date(2026, 2, 17), 'absent'),
    (subjects[2], date(2026, 2, 18), 'present'),
    (subjects[3], date(2026, 2, 19), 'present'),
]

for subject, record_date, status in records_data:
    record, created = AttendanceRecord.objects.get_or_create(
        user=user,
        subject=subject,
        date=record_date,
        defaults={'status': status}
    )
    status_text = "Created" if created else "Already exists"
    print(f"   ✓ {status_text}: {subject.name} on {record_date} - {status}")

# Show summary
print("\n" + "=" * 60)
print("DATABASE SUMMARY")
print("=" * 60)
print(f"Users: {User.objects.count()}")
print(f"Subjects: {Subject.objects.count()}")
print(f"Lectures: {Lecture.objects.count()}")
print(f"Attendance Records: {AttendanceRecord.objects.count()}")
print(f"User Settings: {UserSetting.objects.count()}")

print("\n" + "=" * 60)
print("TEST DATA CREATED SUCCESSFULLY!")
print("=" * 60)
print("\nYou can now:")
print("1. Refresh pgAdmin (right-click Tables → Refresh)")
print("2. Click on any table to see the data")
print("3. Login to the app with:")
print("   Email: test@example.com")
print("   Password: test123")
print("\n" + "=" * 60)
