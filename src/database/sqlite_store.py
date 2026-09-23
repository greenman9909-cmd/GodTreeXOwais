import sqlite3

class SQLiteStore:
    def __init__(self, path='godtree.db'):
        self.connection = sqlite3.connect(path)

    def execute(self, query, params=()):
        return self.connection.execute(query, params)
