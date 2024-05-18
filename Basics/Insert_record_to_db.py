# Insert into table - To fill a table in MySQL, use the "INSERT INTO" statement.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES(%s, %s)"
val = ("Ravi", "Bengaluru")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")