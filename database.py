import sqlite3

def connect_db():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        flight_number TEXT NOT NULL,
        departure TEXT NOT NULL,
        destination TEXT NOT NULL,
        date TEXT NOT NULL,
        seat_number TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()
