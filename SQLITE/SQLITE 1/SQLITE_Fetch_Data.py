import sqlite3

db_connection = sqlite3.connect("Sqlite_work")
#cursor object
cursor = db_connection.cursor()

fetchData = """
select * from customers
"""

cursor.execute(fetchData)
data = cursor.fetchall()
print(data)