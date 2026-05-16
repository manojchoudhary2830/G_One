import sqlite3

from core.config import DATABASE_PATH


class MemoryDB:
    def __init__(self, db_path=DATABASE_PATH):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            content TEXT
        )
        ''')

        self.conn.commit()

    def save(self, role, content):
        self.cursor.execute(
            "INSERT INTO memory(role, content) VALUES (?, ?)",
            (role, content)
        )
        self.conn.commit()

    def fetch_recent(self, limit=10):
        self.cursor.execute(
            "SELECT role, content FROM memory ORDER BY id DESC LIMIT ?",
            (limit,)
        )

        rows = self.cursor.fetchall()
        rows.reverse()

        return [{"role": r, "content": c} for r, c in rows]
