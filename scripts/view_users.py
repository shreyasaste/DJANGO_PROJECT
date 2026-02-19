"""
View All Users Script
This script displays all users and their data statistics.
"""

import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_backend.settings')
django.setup()

from django.contrib.auth.models import User
from attendance.models import Subject, Lecture, AttendanceRecord, UserSetting


def main():
    print("\n" + "="*80)
    print("ALL USERS - Attendance Manager")
    print("="*80)
    
    users = User.objects.all()
    
    if not users:
        print("\n❌ No users found in the database.")
        return
    
    print(f"\nTotal Users: {users.count()}\n")
    
    for user in users:
        # Get user stats
        subjects = Subject.objects.filter(user=user)
        lectures = Lecture.objects.filter(user=user)
        records = AttendanceRecord.objects.filter(user=user)
        
        # Calculate attendance stats
        total_records = records.count()
        present = records.filter(status='present').count()
        absent = records.filter(status='absent').count()
        off = records.filter(status='off').count()
        
        attendance_pct = 0
        if present + absent > 0:
            attendance_pct = round((present / (present + absent)) * 100, 1)
        
        print("-"*80)
        print(f"👤 User ID: {user.id}")
        print(f"   Username: {user.username}")
        print(f"   Email: {user.email}")
        print(f"   Name: {user.first_name or 'N/A'}")
        print(f"   Date Joined: {user.date_joined.strftime('%Y-%m-%d %H:%M')}")
        print(f"   Last Login: {user.last_login.strftime('%Y-%m-%d %H:%M') if user.last_login else 'Never'}")
        print(f"\n📊 Data Statistics:")
        print(f"   Subjects: {subjects.count()}")
        print(f"   Lectures: {lectures.count()}")
        print(f"   Attendance Records: {total_records}")
        print(f"      - Present: {present}")
        print(f"      - Absent: {absent}")
        print(f"      - Off: {off}")
        print(f"   Overall Attendance: {attendance_pct}%")
        
        if subjects.exists():
            print(f"\n📚 Subjects:")
            for subject in subjects:
                sub_records = records.filter(subject=subject)
                sub_present = sub_records.filter(status='present').count()
                sub_absent = sub_records.filter(status='absent').count()
                sub_pct = 0
                if sub_present + sub_absent > 0:
                    sub_pct = round((sub_present / (sub_present + sub_absent)) * 100, 1)
                print(f"      - {subject.name} ({subject.code or 'No code'}): {sub_pct}% ({sub_present}P/{sub_absent}A)")
        
        print()
    
    print("="*80)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
