-- Task 2: Write a Python script to insert a new record into a database table using SQLite3.

import sqlite3

def insert_record():
    conn = sqlite3.connect("manishdb.db")
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        age INTEGER
    )""")
    
    # Insert a new record
    cursor.execute("""
    INSERT INTO Users (name, email, age)
    VALUES ('Manish', 'manish@rps.com', 28)
    """)
    
    conn.commit()
    conn.close()

insert_record()
