# CREATE USER raj@localhost IDENTIFIED BY 'raj123';
# GRANT ALL PRIVILEGES ON newdb.* TO raj@localhost;
import mysql.connector
conn=mysql.connector.connect(host='localhost', password='shree@123', user='shree')

if conn.is_connected():
    print("Connected!!!")
