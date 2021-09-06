import json
#used to read and write directly from JSON files
from difflib import get_close_matches
#difflib a library that compares texts
#get_close_matches() is a function in the library

data = json.load(open('data.json'))
#downloading data into a data type

#functions, conditionals, and input
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA 
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        #this is a list object
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        #a string format and get the first element of a list
        #the users response gets stored in a variable 
        if yn.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn.lower() == "n":
            return "The words does not exist."
        else:
            return "We do not understand your input"
    else:
        return "the word does not exist"

word = input('Enter word: ')
#print out each definitions seperately by line. 
#first create a variable then a function to print items out seperately 
output = (translate(word)) 

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

