#!/usr/bin/env python3
"""
Check authentication and attendance data in database
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_backend.settings')
django.setup()

from django.contrib.auth.models import User
from attendance.models import Subject, Lecture, AttendanceRecord, UserSetting

print("=" * 70)
print("AUTHENTICATION & ATTENDANCE DATA")
print("=" * 70)

# Show users with their authentication data
print("\n🔐 USERS (Authentication Data):")
print("-" * 70)
print(f"{'ID':<5} {'Username (Email)':<30} {'Name':<20} {'Active':<8}")
print("-" * 70)
for user in User.objects.all():
    print(f"{user.id:<5} {user.username:<30} {user.first_name:<20} {'Yes' if user.is_active else 'No':<8}")

# Show attendance records with details
print("\n✅ ATTENDANCE RECORDS (Marked Attendance):")
print("-" * 70)
print(f"{'ID':<5} {'User':<20} {'Subject':<20} {'Date':<12} {'Status':<10}")
print("-" * 70)
for record in AttendanceRecord.objects.select_related('user', 'subject').all().order_by('-date'):
    print(f"{record.id:<5} {record.user.username[:18]:<20} {record.subject.name[:18]:<20} {str(record.date):<12} {record.status:<10}")

# Show subjects per user
print("\n📚 SUBJECTS PER USER:")
print("-" * 70)
for user in User.objects.all():
    subjects = Subject.objects.filter(user=user)
    print(f"\n{user.username} ({user.first_name}):")
    for subject in subjects:
        records = AttendanceRecord.objects.filter(subject=subject)
        present = records.filter(status='present').count()
        absent = records.filter(status='absent').count()
        total = present + absent
        percentage = (present / total * 100) if total > 0 else 0
        print(f"  - {subject.name}: {present}/{total} ({percentage:.0f}%)")

# Show today's attendance
from datetime import date
today = date.today()
print(f"\n📅 TODAY'S ATTENDANCE ({today}):")
print("-" * 70)
today_records = AttendanceRecord.objects.filter(date=today).select_related('user', 'subject')
if today_records.exists():
    for record in today_records:
        status_emoji = "✅" if record.status == 'present' else "❌" if record.status == 'absent' else "➖"
        print(f"{status_emoji} {record.user.username}: {record.subject.name} - {record.status.upper()}")
else:
    print("No attendance marked for today yet.")

print("\n" + "=" * 70)
print("SUMMARY:")
print("=" * 70)
print(f"Total Users: {User.objects.count()}")
print(f"Total Subjects: {Subject.objects.count()}")
print(f"Total Attendance Records: {AttendanceRecord.objects.count()}")
print(f"Records Today: {AttendanceRecord.objects.filter(date=today).count()}")
print("=" * 70)

print("\n📍 WHERE DATA IS STORED:")
print("-" * 70)
print("Authentication Data → auth_user table")
print("  - username (email)")
print("  - password (hashed)")
print("  - first_name (user's name)")
print("  - is_active, date_joined, etc.")
print()
print("Attendance Data → attendance_attendancerecord table")
print("  - user_id (who marked it)")
print("  - subject_id (which subject)")
print("  - date (when)")
print("  - status (present/absent/off)")
print("  - lecture_time (optional)")
print("=" * 70)
