#simple list comprehension - when it comes to large data, it is the programers job to to save bytes
    #example: 
    temps = [221,234,340,230]
    #this will store less data compared
    temps = [22.1,23.4....]
    #how do we convert the . by / it by 10

    #long way
    #create a new list empty list
        new_temps = []
        for temp in temps:
            new_temps.append(temp/10)
        #diving 10 to every item on list and adding it to the new list
        print(new_temps)
    
    #short way (list comprehension)
    #not creating an empty list, but a dynamic list
    temps = [221,234,340,230]
    new_temps = [temp/10 for temp in temps]
    print(new_temps)

#list comprehension with conditionals

    temps = [221,234,340,-999,230]
    #how to create a new list that does not include outliers(-999)
    new_temps = [temp/10 for temp in temps if temp != -999]
    #output [22.1,23.4,34.0,23.0]

#excersice
    #define function takes as a parameter a list(str and int) and returns list only int

    def foo(lst):
        return [i for i in lst if isinstance(i, int)]

#list comprehensions with if-else conditional
    new_temps = [temp / 10 if temp != -999 else 0 for temp in temps]
    #here we stated give me temp divide by 10 of if temp is different than (-999) else give me 0 for temp in temps
    #the for loop goes at the end

#excersice
    #define function takes a list (# and str) returns list with 0 instead of str.
    def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst ]

#excersice: convert and sum
    #define functiontakes list with decimals as str and returns the sum of #
    def foo(lst):
    return sum([float(i) for i in lst])

#review

    #A list comprehension is an expression that creates a list by iterating over another container.

    #A basic list comprehension:

        [i*2 for i in [1, 5, 10]]
        Output: [2, 10, 20]

    #List comprehension with if condition:

        [i*2 for i in [1, -2, 10] if i>0]
        Output: [2, 20]

    #List comprehension with an if and else condition:

        [i*2 if i>0 else 0 for i in [1, -2, 10]]
        Output: [2, 0, 20]


