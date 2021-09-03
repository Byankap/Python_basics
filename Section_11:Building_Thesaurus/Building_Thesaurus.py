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
    elif len(get_close_matches(word, data.keys())) > 0:
        #this is a list object
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        #a string format and get the first element of a list
        #the users response gets stored in a variable 
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
    else:
        return "the word does not exist"

word = input('Enter word: ')

print(translate(word)) 

