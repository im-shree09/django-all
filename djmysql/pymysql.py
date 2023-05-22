import mysql.connector
conn=mysql.connector.connect(host='localhost', password='shree@123', user='shree')

if conn.is_connected():
    print("Connected!!!")