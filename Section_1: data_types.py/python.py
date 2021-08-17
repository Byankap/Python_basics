#python3.8 file_name.py (Mac and Linux)
#python3.8 (Mac and Linux)

#printing function
print( 24 * 7)

    #or

    days_of_week = 7
    hours_per_day = 24
    hours_per_week = hours_per_day * days_of_week
    print(hours_per_week)

#data types float = 10.1, int = 10, str = 'hello'

#list[]
    # using a range ex: 
    list(range(1,10))
    #the output will be:
    [1,2,3,4,5,6,7,8,9] 
    '''the 10 is not included on the list, the list always runs up to one number before the upper number'''

    #specify a step as third argument
    list(range(1,10,2))
    #output
    [1,3,5,7,9]

    #tip: a list can also have any data types ex:
    temp = [75.5, 80, '101', [32,43]]

#dir
    '''you can enter dir(str) on the terminal and it will provided all the things you can do (attributes) with that data type''' 
    # can also type help(st.upper) to learn how to use method

#.upper()
    #caps all letters
    'hello'.upper()
    #output
    'HELLO'

#.lower()
    #ex:
    username = "Python3"
    print(username.lower())

#.title()
    #caps first letter only
    'hello'.title()
    #output
    'Hello'

#sum, length, mean
    student_grades = [9.1, 8.8, 7.5]
    adding_grades = sum(student_grades)
    length = len(student_grades)
    mean = adding_grades/length
    print(mean)
    #output = 8.4666

#max()
    #returns the maximum value, ex:
    student_grades = [9.1, 8.8, 7.5]
    max_value = max(student_grades)
    print(max_value)

#count
    #counts how many values are in a list, ex:
    student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
    list_of_ten = student_grades.count(10.0)
    print(list_of_ten)

#dict
    student_grades = {'Marry' : 9.1, 'Sim': 8.8, 'Jerry': 7.5}
    
    #to find the values
    student_grades.value()
    #output: values([9.1,8.8,7.5])

    #keys
    student_grades.keys()
    #output: values(['Marry'],'Sim','Jerry')


    # wanted to find the mean in a dict
    adding_grades = sum(student_grades.values())
    length = len(student_grades)
    mean = adding_grades/length
    print(mean)
    #output = 8.4666

#tuples
    #like a list but () and you cannot add new things or remove items
    # ex: of tuples inside a dictionary: 
    day_temperatures = {'morning':(3.4,5.6,7.6), 'noon':(4.5,6.7,4.3), 'evening':(9.8,7.6,5.6)}

#.append()
    #add new items to the end of the list, etc.
    temp.append(6) #adding 6 to the existing list temp
    #appending first item of a list onto another list
    workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    weekend = ["Sat", "Sun"]
    workdays.append(weekend[0])

#.remove()
     temp.remove(6) #remove 6 to the existing list temp
        '''tip: To remove one item you should apply the remove() method once. To remove three items you should apply the remove() method three times.'''
            seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
            seconds.remove(1.4534345567)
            seconds.remove(1.023458894)
            seconds.remove(1.10001399445)           
# Review

# Integers are for representing whole numbers:

     rank = 10
     eggs = 12
     people = 3

# Floats represent continuous values:

     temperature = 10.2
     rainfall = 5.98
     elevation = 1031.88

# Strings represent any text:

     message = "Welcome to our online shop!"
     name = "John"
     serial = "R001991981SW"

# Lists represent arrays of values that may change during the course of the program:

     members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
     pixel_values = [252, 251, 251, 253, 250, 248, 247]

# Dictionaries represent pairs of keys and values:

     phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
     volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}

# Keys of a dictionary can be extracted with:

     phone_numbers.keys()

# Values of a dictionary can be extracted with:

     phone_numbers.values()

# Tuples represent arrays of values that are not to be changed during the course of the program:

     vowels = ('a', 'e', 'i', 'o', 'u')
     one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# To find out what attributes a type has:

     dir(str)
     dir(list)
     dir(dict)

# To find out what Python builtin functions there are:

     dir(__builtins__)

# Documentation for a Python command can be found with:

     help(str)
     help(str.replace)
     help(dict.values)