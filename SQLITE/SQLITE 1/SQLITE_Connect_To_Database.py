import sqlite3

db_connection = sqlite3.connect("Sqlite_work")
#cursor object
cursor = db_connection.cursor()

createTable = """create table if not exists customers(
customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
phone TEXT NOT NULL,
country TEXT NOT NULL
)
"""
cursor.execute(createTable)
db_connection.commit()

