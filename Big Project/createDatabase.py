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
cursor.execute(sql)
