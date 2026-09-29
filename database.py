import os
import sqlite3
from datetime import datetime

# Define base and data directory paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "waste.db")

def init_db():
    """Initialize SQLite database and create waste_history table if it does not exist."""
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS waste_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            waste_item TEXT NOT NULL,
            category TEXT NOT NULL,
            disposal_method TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_history(waste_item: str, category: str, disposal_method: str):
    """Save an analysis record into the waste_history table."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO waste_history (date, waste_item, category, disposal_method)
        VALUES (?, ?, ?, ?)
    ''', (current_date, waste_item, category, disposal_method))
    conn.commit()
    conn.close()

def get_history():
    """Fetch all stored waste analysis records ordered by newest first."""
    if not os.path.exists(DB_PATH):
        init_db()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, date, waste_item, category, disposal_method 
        FROM waste_history 
        ORDER BY id DESC
    ''')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
