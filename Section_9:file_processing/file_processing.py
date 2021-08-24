#reading text from a file
    #start by storeing the file in a variable
    myfile = open()
    #the open function is what creates file objects
    #the input to the open function is the path to that file (if the file is in the same directory)
    myfile = open('fruits.txt')

    # .read() method, no argurments are needed, it how to read a file in python 
    myfile = open('fruits.txt')
    print(myfile.read())

#file cursor
    #difficult to print somehting twice because after the first time the cursor is at the 
    #bottom, you will need to create a loop or variable. 

#Closing a file
    #creating it and closing it
    myfile = open('fruits.txt')
    content = myfile.read()
    myfile.close()

    print(content)

# Opening Files Using "with"
    #so far the code below is the same as to the first row above 
    #except there is an indentation and the clost function is not necessary it is implicit 
    with open('fruit.txt') as myfile:
        content = myfile.read()
    print(content)

#Different Filepaths
    # need to specify the complete path to the file 
    with open('files/fruit.txt') as myfile:
        content = myfile.read()
    print(content)

#Writing Text to a File
    #for reading a file you write 
    with open('files/fruit.txt', 'r') as myfile:
    #read methods looks for existing files
    
    #for writing 
    with open('files/fruit.txt', 'w') as myfile:
        myfile.write('tomato')
    #no variable is necessary since we are no retriving informaiton
    #writing methods creates new files 
    #if you write 'w' to an existing file, it will overwrite it. 

    #writing more content by using \n for spaces
    with open('files/fruit.txt', 'w') as myfile:
        myfile.write('tomato\nCucumber\nOnion')

    #output
    1. tomato
    2. Cucumber
    3. Onion

#excersice
    #read the bear.txt file and print out the first 90 characters of its content
        with open('bear.txt') as f:
            for c in f:
                print(c[:90])
        #or
        file = open("bear.txt")
        content = file.read()
        file.close()
        print(content[:90])
    
    #define function gets a string character and a filepath as parameters and returns the 
    # of occurences of that character in the file. 
        def file (character, filepath):
            file = open('bear.txt','r')
            text = file.read()
            return text.count(character)
        print(file('america', 'bear.text'))
        
        #or
        
        def foo(character, filepath="bear.txt"):
            file = open(filepath)
            content = file.read()
            return content.count(character)
    
    #create a first.txt file that contains the first 90 characters of bear.txt
        with open('bear.txt') as file:
            content = file.read()
        with open('first.txt', 'w') as file:
            file.write(content[:90])

#open function
    # character meaning
    #     'r' reading
    #     'w' writing, truncating the file first
    #     'x' create a new file and open it for writing
    #     'a' open for writing, appending to the end of the file 
        # '+' open a disk file for updating (reading and writing)

#Appending text to an existing file 