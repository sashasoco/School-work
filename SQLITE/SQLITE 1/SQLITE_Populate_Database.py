import sqlite3

db_connection = sqlite3.connect("Sqlite_work")
#cursor object
cursor = db_connection.cursor()

addData = """
insert into customers (first_name,last_name,phone,country) values (?,?,?,?)
"""

cursor.execute(addData,('John','Bow','079 443 5448','Egypt'))
db_connection.commit()