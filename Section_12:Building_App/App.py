#creating an app that querie data from mysql database

#downloading a library to allow pyton to interact w/ mysql
# on the terminal type: pip3 intall mysql-connector-python

import mysql.connector

#create a connection using a variable 
con = mysql.connector.connect(
user = 'ardit700_student', 
password = 'ardit700_student',
host = '108.167.140.122',
database = 'ardit700_pm1database'   
)

#create a cursor object used to navigate through the table of database
cursor = con.cursor()

#create a query
query = cursor.execute('SELECT * FROM Dictionary') #here goes sql statement

#getting the data
results = cursor.fetchall()

print(results)