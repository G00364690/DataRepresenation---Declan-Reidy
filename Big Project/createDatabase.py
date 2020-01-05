import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="datarepresentation",
    autocommit=True
)

cursor = db.cursor()

sql = "CREATE TABLE test3 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"
# This does not update the sql localhost as expected. 
#The code cannot be run again with same table name as the database/table are created
# But they do not appear under show tables.

cursor.execute(sql)
