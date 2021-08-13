#fucntions
    #previously determine the mean by:
    student_grades = [9.1, 8.8, 7.5]
    adding_grades = sum(student_grades)
    length = len(student_grades)
    mean = adding_grades/length
    print(mean)
    #output = 8.4666

    #creating own mean function
    #skeleton
    def name_of_function(parameters): #parameters are inputs that function will get and process for an output

    def mean(my_list):
        #calculate the mean
        the_mean = sum(my_list) / len(my_list)
        return the_mean
    
    print(mean(1,3,5)))

#conditionals
    #what if we wanted to use the same as:
    def mean(my_list):
        #calculate the mean
        the_mean = sum(my_list) / len(my_list)
        return the_mean
    
    print(mean(1,3,5))) #but recognize a dictionary as well

    def mean(my_list):
        if type(value) == dict:
            the_mean = sum(value.value()) / len(value)
        else:
            the_mean = sum(my_list) / len(my_list)
        return the_mean
    
#isinstance()

#review

Define a function:

    def cube_volume(a):
        return a * a * a

Write a conditional block:

    message = "hello there"
 
    if "hello" in message:
        print("hi")
    else:
        print("I don't understand")

Write a conditional block of multiple conditions:

    message = "hello there"
 
    if "hello" in message:
        print("hi")
    elif "hi" in message:
        print("hi")
    elif "hey" in message:
        print("hi")
    else:
        print("I don't understand")

Use the and operator to check if both conditions are True at the same time:

    x = 1
    y = 1
 
    if x == 1 and y==1:
        print("Yes")
    else:
        print("No")

    Output is Yes since both x and y are 1.

Use the or operator to check if at least one condition is True:

    x = 1
    y = 2
 
    if x == 1 or y==2:
        print("Yes")
    else:
        print("No")
    
    Output is Yes since x is 1.

Check if a value is of a particular type with:

    isinstance("abc", str)
    isinstance([1, 2, 3], list)
or

    type("abc") == str
    type([1, 2, 3]) == lst


