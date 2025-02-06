-- Task 1: Create a Python script to connect to a MySQL database and fetch records from a table.


import mysql.connector

def fetch_records():
    conn = mysql.connector.connect(
        host="localhost",
        user="manish18",
        password="Manish@18",
        database="manishdb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")
    records = cursor.fetchall()
    for record in records:
        print(record)
    conn.close()

fetch_records()
