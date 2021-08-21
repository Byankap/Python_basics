#functions with multiple arguments
    def area(a, b):
        return a + b
    print(area(4,5))

#function that takes two str as arguments, concatenates, and return result
    def foo(str1, str2):
        return str1 + str2

    foo('hello', 'Byanka')

#Default and Non-default Default and Non-default
# Parameters and Keyword and Non-…71. Default and Non-default Parameters and Keyword and Non-keyword Arguments
    def area(a, b):
        return a + b
    print(area(4,5))
    #currently 4,5 are non-keyword argruments or
    #positional arguments because positional matters based on the function of position

    print(area(a=4,b=5))
    #keyword arguments

    print(area(b=4,a=5))
    #in this case the position doesnt matter, since its being specified
    #default parameters
    def area(a, b=5):
    #no need to specify it on the print statement, its assumed its there so the output will be 11
    print(area(a=5)) #or
    print(area(5))

    # you can also assign different values to a or b
     print(area(a=5, b=10))

     #important note: a default parameter cannot be before a non-default it will create an error

#Functions with an Arbitrary Number of Non-keyword Arguments
    def mean(*args):
    #to pass as many arguments as you want
        return sum(args) / len(args)
    
#excersice 
    #define function takes indefinite # str and returns list in uppercase and sorted alphaabetically 
    def foo(*args):
        args = [x.upper() for x in args]
        return sorted(args)

#Functions with an Arbitrary Number of Keyword Arguments
    #syntax
    def mean(**kwargs):
        return kwargs
    #if the arguments dont haave key words it will be error
    print(mean(a=1, b=2, c=3))

#review

    #Functions can have more than one parameter:

        def volume(a, b, c):
            return a * b * c

    #Functions can have default parameters (e.g. coefficient):

        def converter(feet, coefficient = 3.2808):
            meters = feet / coefficient
            return meters
 
        print(converter(10))
        Output: 3.0480370641306997

    #Arguments can be passed as non-keyword (positional) arguments (e.g. a) or keyword arguments (e.g. b=2 and c=10):

        def volume(a, b, c):
            return a * b * c
 
        print(volume(1, b=2, c=10))
        
    #An *args parameter allows the  function to be called with an arbitrary number of non-keyword arguments:

        def find_max(*args):
            return max(args)
        print(find_max(3, 99, 1001, 2, 8))
        Output: 1001

    #An **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:

        def find_winner(**kwargs):
            return max(kwargs, key = kwargs.get)
 
        print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
        Output: Sim


