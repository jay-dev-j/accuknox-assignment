import csv
import sqlite3

conn = sqlite3.connect("persons.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS persons (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT)""")

cursor.execute("DELETE FROM persons")

with open("persons.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("INSERT INTO persons (name, email) VALUES (?, ?)",(row["name"], row["email"]))

conn.commit()

cursor.execute("SELECT * FROM persons")

for row in cursor.fetchall():
    print(row)

conn.close()