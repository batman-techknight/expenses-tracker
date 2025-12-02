from db_connection import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
INSERT INTO expenses (date, category, amount, notes)
VALUES (?, ?, ?, ?)
""", ("2025-01-01", "Food", 150.75, "Lunch"))

conn.commit()
conn.close()

print("Test expense added!")