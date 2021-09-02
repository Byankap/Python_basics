import json
#used to read and write directly from JSON files
import difflib
#a library that compares texts

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "the word does not exist"
word = input('Enter word: ')

print(translate(word)) 

