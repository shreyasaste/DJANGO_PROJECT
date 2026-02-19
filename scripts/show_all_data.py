#!/usr/bin/env python3
"""
Display all data from the database
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_backend.settings')
django.setup()

from django.contrib.auth.models import User
from attendance.models import Subject, Lecture, AttendanceRecord, UserSetting

print("=" * 70)
print("ALL DATA IN DATABASE")
print("=" * 70)

# Show users
print("\n📋 USERS:")
print("-" * 70)
for user in User.objects.all():
    print(f"ID: {user.id} | Username: {user.username} | Name: {user.first_name}")

# Show subjects
print("\n📚 SUBJECTS:")
print("-" * 70)
for subject in Subject.objects.all():
    print(f"ID: {subject.id} | Name: {subject.name} | Code: {subject.code} | User: {subject.user.username}")

# Show lectures
print("\n📅 LECTURES (Timetable):")
print("-" * 70)
for lecture in Lecture.objects.all():
    print(f"ID: {lecture.id} | Subject: {lecture.subject.name} | Day: {lecture.day} | Time: {lecture.time}")

# Show attendance records
print("\n✅ ATTENDANCE RECORDS:")
print("-" * 70)
for record in AttendanceRecord.objects.all():
    print(f"ID: {record.id} | Subject: {record.subject.name} | Date: {record.date} | Status: {record.status}")

# Show settings
print("\n⚙️ USER SETTINGS:")
print("-" * 70)
for setting in UserSetting.objects.all():
    print(f"User: {setting.user.username} | Target: {setting.target_percentage}%")

print("\n" + "=" * 70)
print("SUMMARY:")
print("=" * 70)
print(f"Total Users: {User.objects.count()}")
print(f"Total Subjects: {Subject.objects.count()}")
print(f"Total Lectures: {Lecture.objects.count()}")
print(f"Total Records: {AttendanceRecord.objects.count()}")
print(f"Total Settings: {UserSetting.objects.count()}")
print("=" * 70)
