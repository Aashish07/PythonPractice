# For loops are used for sequential traversal. 
# For example: traversing a list or string or array etc.

    # # Python program to illustrate 
    # # Iterating over a list 
    # print("List Iteration") 
    # l = ["geeks", "for", "geeks"] 
    # for i in l: 
    #     print(i) 
            
    # # Iterating over a tuple (immutable) 
    # print("\nTuple Iteration") 
    # t = ("geeks", "for", "geeks") 
    # for i in t: 
    #     print(i) 
            
    # # Iterating over a String 
    # print("\nString Iteration")	 
    # s = "Geeks"
    # for i in s : 
    #     print(i) 
            
    # # Iterating over dictionary 
    # print("\nDictionary Iteration") 
    # d = dict() 
    # d['xyz'] = 123
    # d['abc'] = 345
    # for i in d : 
    #     print("% s % d" %(i, d[i])) 

# Loop Control Statements
    # Loop control statements change execution from its normal sequence.
    # Continue Statement: It returns the control to the beginning of the loop.

    # # Prints all letters except 'e' and 's' 
    # for letter in 'geeksforgeeks': 
    # 	if letter == 'e' or letter == 's': 
    # 		continue
    # 	print('Current Letter :', letter)

# Break Statement: 
    # It brings control out of the loop.  

    # for letter in 'geeksforgeeks': 

    #     # break the loop as soon it sees 'e' 
    #     # or 's' 
    #     if letter == 'e' or letter == 's': 
    #         break

    # print('Current Letter :', letter)

# Pass Statement:
    # We use pass statement to write empty loops. 
    # Pass is also used for empty control statements, function and classes.

    # # An empty loop 
    # for letter in 'geeksforgeeks': 
    #     pass
    # print('Last Letter :', letter)

# range() function :-
    # range() is a built-in function of Python. 
    # It is used when a user needs to perform an action for a specific number of times. 
    # range() in Python(3.x) is just a renamed version of a function called xrange() in Python(2.x)

        # 1. start: integer starting from which the sequence of integers is to be returned 
        # 2. stop: integer before which the sequence of integers is to be returned. 
        # The range of integers end at stop – 1. 
        # 3. step: integer value which determines the increment between each integer in the sequence 

        # # Python Program to
        # # show range() basics

        # # printing a number
        # for i in range(10):
        #     print(i, end=" ")
        # print()

        # # using range for iteration
        # l = [10, 20, 30, 40]
        # for i in range(len(l)):
        #     print(l[i], end=" ")
        # print()

        # # performing sum of first 10 numbers
        # sum = 0
        # for i in range(1, 10):
        #     sum = sum + i
        # print("Sum of first 10 numbers :", sum)

# for-else function :-
    # Note: The else block just after for/while is executed only when the loop is NOT terminated by a break statement 

        # # Python program to demonstrate
        # # for-else loop

        # for i in range(1, 4): 
        # 	print(i) 
        # else: # Executed because no break in for 
        # 	print("No Break\n") 

        # for i in range(1, 4): 
        # 	print(i) 
        # 	break
        # else: # Not executed as there is a break 
        # 	print("No Break") 
