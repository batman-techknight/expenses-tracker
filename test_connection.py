from db_connection import get_connection

try:
    conn = get_connection()
    print("Connected to SQLite DB successfully!")
    conn.close()
except Exception as e:
    print("Error:", e)
