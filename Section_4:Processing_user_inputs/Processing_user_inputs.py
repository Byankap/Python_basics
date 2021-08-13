#user input
    #commands the user to enter a value in order to process it
    input("Enter Temp:")
    #nothing will happend 
    #put it as a variable
    def weather(temp):
        if temp > 7:
            return "warm"
        else:
            return "cold"
    user_input = float(input("Enter temp:"))
    print(weather(user_input))

#string formatting
    user_input = input("Enter your name: ")
    #this message is only valid for python2-3.1 
    message = 'Hello %s' % user_input
    #for python 3.6
    message = f"Hello {user_input}"
    print(message)

#string formatting w/ multiple variables
    #for python 2-3
    first_name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
    message = 'Hello %s %s' % (first_name, last_name)
    
    #for python 3.6
    message = f"Hello {first_name} {last_name}"
    print(message)

#Review
    A Python program can get user input via the input function:

    The input function halts the execution of the program and gets text input from the user:

        name = input("Enter your name: ")

    The input function converts any input to a string, but you can convert it back to int or float:

        experience_months = input("Enter your experience in months: ")
        experience_years = int(experience_months) / 12

    You can format strings with (works both on Python 2 and 3):

        name = "Sim"
        experience_years = 1.5
        print("Hi %s, you have %s years of experience." % (name, experience_years))

        Output: Hi Sim, you have 1.5 years of experience.

    You can also format strings with:

        name = "Sim"
        experience_years = 1.5
        print("Hi {}, you have {} years of experience".format(name, experience_years))

        Output: Hi Sim, you have 1.5 years of experience.

