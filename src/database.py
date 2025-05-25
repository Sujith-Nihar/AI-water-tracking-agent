import sqlite3
from datetime import datetime

DB_NAME = "water_tracker.db"
# DATABASE_URL = 

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS water_intake (
                   Id INTEGER PRIMARY KEY AUTOINCREMENT,
                   UserId TEXT,
                   Intake INTEGER,
                   Date TEXT
                   )

        """)
    
    conn.commit()
    conn.close()


def log_intake(user_id, intake_ml):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    now = datetime.today().strftime('%Y-%m-%d')
    cursor.execute("INSERT INTO water_intake (UserId, Intake, Date) VALUES (?, ?, ?)", (user_id, intake_ml, now))
    conn.commit()
    conn.close()


def get_intake_history(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    now = datetime.today().strftime('%Y-$m-%d')
    cursor.execute("SELECT Intake, Date from water_intake where UserId = ?", (user_id,))
    records = cursor.fetchall()
    conn.close()
    return records


create_tables()