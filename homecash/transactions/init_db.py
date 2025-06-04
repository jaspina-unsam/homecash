import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "homecash.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    type TEXT NOT NULL,
    category TEXT,
    date TEXT NOT NULL,
    description TEXT
);
"""


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(SCHEMA)
        conn.commit()


if __name__ == "__main__":
    init_db()
    print("Base de datos inicializada en:", DB_PATH)
