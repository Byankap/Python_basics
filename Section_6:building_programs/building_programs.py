#creating a program that asks user to type somthing over and over until user 
#enters \end, then prints all the inputs in cap and punctuation marks

    #Step1: creating typical strings into formated strings, w/ cap and punctuation
        def sentence_maker(phase):
            interrogatives = ('how',"what","where","why","when")
            capitalized = phrase.capitalize()
            if phrase.startswith(interrogatives)
                return '{}?'.format(capitalized)
            else:
                return '{}.'.format(capitalized)

        print(sentence_maker('how are you'))
        #output: "How are you?"
        #This is not part of the function - only to show what it can do

    #step2: creating the loop
        #if we want to store all of the inputs, create an empty list
        results = []
        while True:
            user_input = input('Say something: ')
            if user_input == '\end':
                break
            else:
                results.append(sentence_maker(user_input))
            # you dont want to append first or else the /end will get append 


# ''.join()
    contcatinate strings together 
        #ex: "-".join(['how are you', 'good good', 'clear clear'])
        #output = 'how are you-good good-clear clear'. Can also replace the - with a space-better