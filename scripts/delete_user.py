"""
Delete User Data Script
This script allows you to delete a user and all their data from the database.
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


def list_all_users():
    """Display all users in the system"""
    users = User.objects.all()
    if not users:
        print("\n❌ No users found in the database.")
        return []
    
    print("\n" + "="*60)
    print("ALL USERS IN SYSTEM")
    print("="*60)
    print(f"{'ID':<5} {'Username':<20} {'Email':<30} {'Name':<20}")
    print("-"*60)
    
    for user in users:
        name = user.first_name or "N/A"
        print(f"{user.id:<5} {user.username:<20} {user.email:<30} {name:<20}")
    
    print("="*60)
    return users


def get_user_stats(user):
    """Get statistics about user's data"""
    subjects_count = Subject.objects.filter(user=user).count()
    lectures_count = Lecture.objects.filter(user=user).count()
    records_count = AttendanceRecord.objects.filter(user=user).count()
    
    return {
        'subjects': subjects_count,
        'lectures': lectures_count,
        'records': records_count
    }


def delete_user_data_only(user):
    """Delete only user's data, keep the account"""
    stats = get_user_stats(user)
    
    print(f"\n📊 User Data Summary:")
    print(f"   - Subjects: {stats['subjects']}")
    print(f"   - Lectures: {stats['lectures']}")
    print(f"   - Attendance Records: {stats['records']}")
    
    confirm = input("\n⚠️  Delete all this data? (keep account) [yes/no]: ").strip().lower()
    
    if confirm == 'yes':
        Subject.objects.filter(user=user).delete()
        Lecture.objects.filter(user=user).delete()
        AttendanceRecord.objects.filter(user=user).delete()
        UserSetting.objects.filter(user=user).delete()
        
        print(f"\n✅ Successfully deleted all data for user: {user.email}")
        print(f"   Account still exists - user can login with empty data")
        return True
    else:
        print("\n❌ Deletion cancelled.")
        return False


def delete_user_completely(user):
    """Delete user account and all their data"""
    stats = get_user_stats(user)
    
    print(f"\n📊 User Data Summary:")
    print(f"   - Subjects: {stats['subjects']}")
    print(f"   - Lectures: {stats['lectures']}")
    print(f"   - Attendance Records: {stats['records']}")
    
    print(f"\n⚠️  WARNING: This will permanently delete:")
    print(f"   - User account: {user.email}")
    print(f"   - All user data (subjects, lectures, attendance)")
    print(f"   - User will NOT be able to login anymore")
    
    confirm = input("\n⚠️  Are you absolutely sure? Type 'DELETE' to confirm: ").strip()
    
    if confirm == 'DELETE':
        username = user.username
        email = user.email
        user.delete()  # CASCADE will delete all related data
        
        print(f"\n✅ Successfully deleted user account and all data:")
        print(f"   Username: {username}")
        print(f"   Email: {email}")
        return True
    else:
        print("\n❌ Deletion cancelled.")
        return False


def main():
    print("\n" + "="*60)
    print("DELETE USER DATA - Attendance Manager")
    print("="*60)
    
    # List all users
    users = list_all_users()
    if not users:
        return
    
    # Get user selection
    print("\n📝 Select deletion method:")
    print("   1. Delete by Email")
    print("   2. Delete by User ID")
    print("   3. Cancel")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    user = None
    
    if choice == '1':
        email = input("\n📧 Enter user email: ").strip()
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            print(f"\n❌ User with email '{email}' not found.")
            return
    
    elif choice == '2':
        user_id = input("\n🆔 Enter user ID: ").strip()
        try:
            user = User.objects.get(id=int(user_id))
        except (User.DoesNotExist, ValueError):
            print(f"\n❌ User with ID '{user_id}' not found.")
            return
    
    elif choice == '3':
        print("\n❌ Operation cancelled.")
        return
    
    else:
        print("\n❌ Invalid choice.")
        return
    
    # Show user details
    print(f"\n👤 User Found:")
    print(f"   ID: {user.id}")
    print(f"   Username: {user.username}")
    print(f"   Email: {user.email}")
    print(f"   Name: {user.first_name or 'N/A'}")
    
    # Choose deletion type
    print("\n🗑️  What do you want to delete?")
    print("   1. Delete only data (keep account)")
    print("   2. Delete account and all data")
    print("   3. Cancel")
    
    delete_choice = input("\nEnter choice (1-3): ").strip()
    
    if delete_choice == '1':
        delete_user_data_only(user)
    elif delete_choice == '2':
        delete_user_completely(user)
    elif delete_choice == '3':
        print("\n❌ Operation cancelled.")
    else:
        print("\n❌ Invalid choice.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
