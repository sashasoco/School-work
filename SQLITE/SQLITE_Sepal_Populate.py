import sqlite3

connect_to_db = sqlite3.connect('iris.db_work')

db_cursor = connect_to_db.cursor()

addData_to_db = """ insert into irisData (sepal_len,sepal_width,
petal_len,petal_width,class) values (?,?,?,?,?);

"""

f = open('Iris - all-numbers.csv','r')
headerLine = f.readline()
for line in f:
    line=line.strip()#removes the /n
    line=line.split(',')#creates a list - splits on comma
    line=tuple(line)
    
    db_cursor.execute(addData_to_db,line)
    connect_to_db.commit()
#close connections
db_cursor.close()