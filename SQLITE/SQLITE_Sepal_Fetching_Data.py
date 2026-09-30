import sqlite3
import Average_Function

connect_to_db = sqlite3.connect('iris.db_work')

db_cursor = connect_to_db.cursor()

get_data_from_db = """
select sepal_len from irisData;
"""

db_cursor.execute(get_data_from_db)
data = db_cursor.fetchall()

sepal_len_list = []
for data_point in data:
    sepal_len_list.append(data_point[0])
print(sepal_len_list)

average_sepal_len = Average_Function.calc_average(sepal_len_list)

print(f"The average sepal len is: {average_sepal_len}")

db_cursor.close()
connect_to_db.close()