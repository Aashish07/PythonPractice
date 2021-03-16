# Different looping techniques using Python data structures  are: 

    # 1. Using enumerate():
        # enumerate() is used to loop through the containers printing the index number along with the value present in that particular index.
            # # python code to demonstrate working of enumerate() 

            # for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']): 
            #     print(key, value) 
        # Enumerate takes parameter start which is default set to zero. We can change this parameter to any value we like. 
        # In the below code we have used start as 1.

            # # demonstrating the use of start in enumerate 

            # cars = ["Aston" , "Audi", "McLaren "] 
            # for x in enumerate(cars, start=1): 
            #     print (x[0], x[1]) 


    # 2. Using zip():
        # zip() is used to combine 2 similar containers(list-list or dict-dict) printing the values sequentially.
        # The loop exists only till the smaller container ends. 

            # # python code to demonstrate working of zip() 

            # # initializing list 
            # questions = ['name', 'colour', 'shape'] 
            # answers = ['apple', 'red', 'a circle'] 

            # # using zip() to combine two containers 
            # # and print values 
            # for question, answer in zip(questions, answers): 
            # 	print('What is your {0}? I am {1}.'.format(question, answer)) 


    # 3. Using iteritem():
        # iteritems() is used to loop through the dictionary printing the dictionary key-value pair sequentially.

    4. Using items():

    # 5. Using sorted():
        # sorted() is used to print the container is sorted order. 
        # It doesn’t sort the container but just prints the container in sorted order for 1 instance. 
        # The use of set() can be combined to remove duplicate occurrences.

        #     # python code to demonstrate working of sorted() 

        # # initializing list 
        # lis = [ 1 , 3, 5, 6, 2, 1, 3 ] 

        # # using sorted() to print the list in sorted order 
        # print ("The list in sorted order is : ") 
        # for i in sorted(lis) : 
        #     print (i,end=" ") 
            
        # print ("\r") 
            
        # # using sorted() and set() to print the list in sorted order 
        # # use of set() removes duplicates. 
        # print ("The list in sorted order (without duplicates) is : ") 
        # for i in sorted(set(lis)) : 
        #     print (i,end=" ") 


6. Using reversed():
    reversed() is used to print the values of the container in the reversed order. It does not reflect any changes to the original list