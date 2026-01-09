import sqlite3
import os

DB_NAME = "medplus.db"

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()
        self.create_tables()

    def connect(self):
        try:
            self.conn = sqlite3.connect(DB_NAME)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")

    def create_tables(self):
        # Users table (Admin/User)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('USER', 'ADMIN'))
            )
        """)

        # Hospitals table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS hospitals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                contact TEXT NOT NULL
            )
        """)

        # Emergency Contacts table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS emergency_contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact_no TEXT NOT NULL
            )
        """)
        
        # User Personal Contacts table (for specific users if needed, or global)
        # The original code had "Contact_List" for users. Let's keep it simple for now.
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS personal_contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact_no TEXT NOT NULL
            )
        """)
        
        self.conn.commit()

    def execute_query(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor
        except sqlite3.Error as e:
            print(f"Query error: {e}")
            return None

    def fetch_one(self, query, params=()):
        cursor = self.execute_query(query, params)
        return cursor.fetchone() if cursor else None

    def fetch_all(self, query, params=()):
        cursor = self.execute_query(query, params)
        return cursor.fetchall() if cursor else []

    def close(self):
        if self.conn:
            self.conn.close()

# Singleton instance
db = Database()
