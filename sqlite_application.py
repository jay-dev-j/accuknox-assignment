import requests
import sqlite3

# API from (https://openlibrary.org/developers/api)
url = "https://openlibrary.org/subjects/animals.json?limit=10"

# Checking the api request is successful or not

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
    print("Failed to fetch data from API")
    exit()

conn = sqlite3.connect("works.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS works (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,author TEXT,year INTEGER)""")
cursor.execute("DELETE FROM works")
for book in data["works"]:
    title = book.get("title", "Unknown")

    if book.get("authors"):
        author = book["authors"][0]["name"]
    else:
        author = "Unknown"

    year = book.get("first_publish_year","unknown")

    cursor.execute("INSERT INTO works (title, author, year) VALUES (?, ?, ?)",(title, author, year))

conn.commit()

cursor.execute("SELECT * FROM works")

for row in cursor.fetchall():
    print(row)

conn.close()