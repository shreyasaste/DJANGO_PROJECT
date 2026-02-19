import psycopg2

try:
    # Connect to default postgres database
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='87654321',
        host='localhost',
        port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    
    # Check if attendance_manager exists
    cursor.execute("SELECT 1 FROM pg_database WHERE datname='attendance_manager'")
    exists = cursor.fetchone()
    
    if exists:
        print("✓ Database 'attendance_manager' exists!")
    else:
        print("✗ Database 'attendance_manager' does NOT exist")
        print("\nCreating database...")
        cursor.execute("CREATE DATABASE attendance_manager")
        print("✓ Database 'attendance_manager' created successfully!")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Error: {e}")
