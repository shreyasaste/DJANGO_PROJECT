import psycopg2

try:
    # Connect to attendance_manager database
    conn = psycopg2.connect(
        dbname='attendance_manager',
        user='postgres',
        password='87654321',
        host='localhost',
        port='5432'
    )
    
    cursor = conn.cursor()
    
    # List all tables
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
        ORDER BY table_name;
    """)
    
    tables = cursor.fetchall()
    
    print("=" * 60)
    print("TABLES IN 'attendance_manager' DATABASE:")
    print("=" * 60)
    
    if tables:
        for i, table in enumerate(tables, 1):
            print(f"{i}. {table[0]}")
            
            # Count rows in each table
            cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
            count = cursor.fetchone()[0]
            print(f"   Rows: {count}")
    else:
        print("No tables found!")
        print("\nThis means migrations haven't been run yet.")
        print("Run: python manage.py migrate")
    
    print("\n" + "=" * 60)
    print(f"Total tables: {len(tables)}")
    print("=" * 60)
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Error: {e}")
    print("\nMake sure:")
    print("1. PostgreSQL is running")
    print("2. Database 'attendance_manager' exists")
    print("3. Password is correct")
