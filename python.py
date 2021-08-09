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