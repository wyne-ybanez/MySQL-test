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
        list_of_names = ['fred','Fred']
        # format function used to prepare string
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names) 
        connection.commit()

finally:
    # Make sure to close connection
    connection.close()
