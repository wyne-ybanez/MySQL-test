import os 
import pymysql
import datetime

# Get username from Gitpod workspace 
# (Modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to Database
connection = pymysql.connect(host = 'localhost', 
                             user = username,
                             password = '',
                             db = "Chinook") 

try:
    # Run Query
    with connection.cursor() as cursor:
        rows = [(23, 'Bob'),
                (24, 'Jim'),
                (25, 'Fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
                        rows) 
        connection.commit()
finally:
    # Make sure to close connection
    connection.close()
