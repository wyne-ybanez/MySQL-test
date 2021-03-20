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
        row = ("Bob", 21, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES(%s, %s, %s);", row) 
        connection.commit()
finally:
    # Make sure to close connection
    connection.close()
