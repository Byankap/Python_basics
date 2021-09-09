#creating an app that querie data from mysql database

#downloading a library to allow pyton to interact w/ mysql
# on the terminal type: pip3 intall mysql-connector-python

import mysql.connector

#a library that compares text
from difflib import get_close_matches

#create a connection using a variable 
con = mysql.connector.connect( #here are the credientials of database
user = 'ardit700_student', 
password = 'ardit700_student',
host = '108.167.140.122',
database = 'ardit700_pm1database'   
)

#create a cursor object used to navigate through the table of database
cursor = con.cursor()

word = input('Enter a word: ')

#create a query
query = cursor.execute('SELECT * FROM Dictionary WHERE Expression = "%s"' % word) #here goes sql statement

#getting the data
results = cursor.fetchall()

#extracting the tuples from the results so it shows up as a list
if results:
    for result in results:
        print(result[1]) #by adding a one, the second item(definition) is selected w/0 formatted as a tuple/str
         
else:
    print('No word found, sorry')

#implemented code from section 11, get_close_matches
def dictionary (word):
    if result in results:
        print(result[1])
    
    elif len(get_close_matches(word, data.keys())) > 0
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no" %s word)
        if yn.lower() =='y':
            return data[get_close_matches(word,data.keys())[0]]
        elif yn.lower() =='n':
            return ''