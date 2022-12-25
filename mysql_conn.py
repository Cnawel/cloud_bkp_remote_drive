# import mysql.connector

# print("Connecting to DB")

# cnx = mysql.connector.connect(
#                                 user='', 
#                                 password='',
#                                 host='',
#                                 database=''
#                             )
# print("Connected to DB !")

# cnx.close()

# print("Exited DB")

import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='', 
                                password='',
                                host='',
                                port='3306',
                                database='')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()