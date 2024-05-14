import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
)

mycursor = mydb.cursor()

#create table
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") 

#show tables
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)