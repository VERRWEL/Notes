import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', password='', database='db_pytest')

if connection.is_connected():
    print('Connected to MySQL database')
else:
    print('Failed to connect to MySQL database')

mycursor = connection.cursor()

mycursor.execute("CREATE DATABASE nathanraffael")

connection.close()