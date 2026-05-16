from database.memory_db import MemoryDB

class MemoryManager:
    def __init__(self):
        self.db = MemoryDB()

    def save_user_message(self, text):
        self.db.save("user", text)

    def save_ai_message(self, text):
        self.db.save("assistant", text)

    def get_history(self):
        return self.db.fetch_recent()
