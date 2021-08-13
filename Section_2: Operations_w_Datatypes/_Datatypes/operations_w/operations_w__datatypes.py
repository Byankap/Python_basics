#clear
    #in a list, it clears all of the content inside of a list
    temp.clear()
    #when you call out the list, output is an empty []

#index
    #lists have indexing
    #help(index) index(self, value, start=0, stop=9223...)
    temp.index(8.8) #output it will return the #of the index
    #or typing temp[1] to get the value 8.8

    #obtaining a range
    temp[1:4] #it will get the 2nd,3rd, and 4th item but not the 5th
    #ex if we want the first two items:
    temp[0:2] #or short cut temp[:2]
    temp[-1] #gives you the last item on the list
    temp[-2] #gives you the last two items of the list
    'abcdef'[-2:] #output will be 'ef'
    
    #slicing strings
    temp = ['hello', 1,2]
    temp[0][2] #the output will be 'l'

#converting b/t data types
    Sometimes you might need to convert between different data types in Python for one reason or another. That is very easy to do:

    From tuple to list:
    >>> data = (1, 2, 3)
    >>> list(data)
    [1, 2, 3]
    
    From list to tuple:
    >>> data = [1, 2, 3]
    >>> tuple(data)
    (1, 2, 3)
    
    From list to dictionary:
    >>> data = [["name", "John"], ["surname", "smith"]]
    >>> dict(data)
    {'name': 'John', 'surname': 'smith'}
    
    Note that the original data type needs to have the data structured in a way that can be understood by the new data type. For example, the following would not work:
    >>> data = [1, 2, 3]
    >>> dict(data)
    TypeError: cannot convert dictionary update sequence element #0 to a sequence
    That's because a dictionary is made of key and value pairs, but the list was not constructed that way, so the above would generate an error.    

#review
    
Lists, strings, and tuples have a positive index system:
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6

And a negative index system:
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4     -3     -2     -1

In a list, the 2nd, 3rd, and 4th items can be accessed with:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
Output: ['Tue', 'Wed', 'Thu']

First three items of a list:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
Output:['Mon', 'Tue', 'Wed'] 

Last three items of a list:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
Output: ['Fri', 'Sat', 'Sun']

Everything but the last:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 

Everything but the last two:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 

A single in a dictionary can be accessed using its key:
phone_numbers = {"John Smith":"+37682929928","Marry Simpsons":"+423998200919"}
phone_numbers["Marry Simpsons"]
Output: '+423998200919'