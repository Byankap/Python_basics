
#make a program that rounds each temp
    monday_temp = [9.1,5.6,7.3]
    for temp in monday_temp:
        print(round(temp))

#For Loop Over a Function
    #Note that using loops, you can call any function multiple times, even your own functions. Let's suppose we defined this function:

    def celsius_to_kelvin(cels):
        return cels + 273.15    
    #That is a function that gets a number as input, adds 273.15 to it and returns the result. A for loop allows us to execute that function over a list of numbers:

    monday_temperatures = [9.1, 8.8, -270.15]
 
    for temperature in monday_temperatures:
        print(celsius_to_kelvin(temperature))
    #The output of that would be:

        282.25
        281.95
        3.0
    #So, in the first iteration celsius_to_kelvin(9.1) was executed, in the second celsius_to_kelvin(8.8) and in the third celsius_to_kelvin(-270.15).

#Looping through dictionaries
    student_grades = {'marry':9.1, 'Sasha':9.7, 'Mickey':5.6}
     #iterating over items    
    for grades in student_grades.items():
        print(grades)
    #output is items as a tuple
    ('marry', 9.1)
    ('Sasha', 9.7)....etc. 
    #you can print out the items, keys, or values

#Dictionary Loop and String Formatting
    #You can combine a dictionary for loop with string formatting to create text containing information from the dictionary:

    phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
    for pair in phone_numbers.items():
        print("{} has as phone number {}".format(pair[0], pair[1]))


    #Another (better) way to do it::

    phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
    for key, value in phone_numbers.items():
        print("{} has as phone number {}".format(key, value))
    
    #In both cases the output is:

    John Smith has as phone number +37682929928
    Marry Simpons has as phone number +423998200919

type()
    #changes the type

.replace()
    # replaces values with other values 

#while loops
    #run as long as the condition is true
    #ex:
    username = ''

    while username != 'pypy':
        username = input('Enter username: ')
    #or using a While true with break and continue 

    while true:
    #the first situation occurs because true is true
        username = input('Enter username:')
        if username == 'pypy':
            break
        else:
            continue

#review
    #loops are useful for executing a command over a large # of items
    for letter in 'abc':
        print(letter.upper())
    #output
    ABC (vertically)
    #the name after for (letter) is just a variable name

#looping over dictionary keys:
        phone_number = {'Marry': +1234567,'Allen'}
        for value in phone_number.keys():
            print(value)
        #output: Marry and Allen
        #same cam be done for values and items 

#while loops
    #will continue to run as long as a condition is true
    while datetime.datetime.now() < datetime.datetime(2090)
        print('It not yet 19:30:20 of 2090.8.20')