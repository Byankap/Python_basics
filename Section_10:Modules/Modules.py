#Buildin modules, importing modelules for excecuting things not found in python
    #for example time(which contains various attributes.)
        import time
        while true: 
            with open('files/vegetables.txt') as file:
                print(file.read())
                time.sleep(10)
    #the output it will print out the content then wait 10 and do it again.

    #what happens if the file gets deleted or crashes
        import time
        import os
        while true: 
            if.os.path.exists('file/vegetable.txt')
            #os is a python module not found in the buildin module with a lot of attributes, path being one of them (checking to see if a document exist in directory)
                with open('files/vegetables.txt') as file:
                    print(file.read())
            else:
                print('file does not exist')        
            time.sleep(10)

#third party modules
    import pandas
    #check its cotents by:
    #command line type:
    import sys
    sys.prefix
    #copy the url /library/framework/python etc.
    #a window pops up to gain access to folder (site.packages)

    #excercise Pandas
    #have a document ('files/temp_today.csv') with two columns of temp morning, afternoon, night of two days
    #want to know the average temp per day
    import time
    import os
    import pandas

    while True:
        if so.path.exists ('files/temp_today.csv'):
            data = pandas.read_csv('files/temp_today.csv')
            print(data.mean())
        else:
            print('File does not exist.')
            time.sleep(10)
        #if you wanted to know the average for only the first column, update:
        print(data.mean())['st1'])

#review

    #Builtin objects are all objects that are written inside the Python interpreter in C language.

    #Builtin modules contain builtins objects.

    #Some builtin objects are not immediately available in the global namespace. They are parts of a builtin module. To use those objects the module needs to be imported first. E.g.:

        import time
        time.sleep(5)

    #A list of all builtin modules can be printed out with:

        import sys
        sys.builtin_module_names

    #Standard libraries is a jargon that includes both builtin modules written in C and also modules written in Python.

    #Standard libraries written in Python reside in the Python installation directory as .py files. You can find their directory path with sys.prefix.

    #Packages are a collection of .py modules.

    #Third-party libraries are packages or modules written by third-party persons (not the Python core development team).

    #Third-party libraries can be installed from the terminal/command line:

    #Windows:

        #pip install pandas or use python -m pip install pandas if that doesn't work.

    #Mac and Linux:

        #pip3 install pandas or use python3 -m pip install pandas if that doesn't work.


