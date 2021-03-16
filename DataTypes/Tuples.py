# A tuple is a sequence of immutable Python objects. 
# Tuples are just like lists with the exception that tuples cannot be changed once declared. 
# Tuples are usually faster than lists.


    tup = (1, "a", "string", 1+2) 
    print(tup) 
    print(tup[1]) 


    #  Output :-
    (1, 'a', 'string', 3)
    a

# Tuple is a collection of Python objects much like a list. 
# The sequence of values stored in a tuple can be of any type, and they are indexed by integers. 


# -----------------------------Creating a Tuple--------------------------
    # In Python, tuples are created by placing a sequence of values separated by ‘comma’ 
    # with or without the use of parentheses for grouping the data sequence.

    # Note: Creation of Python tuple without the use of parentheses is known as Tuple Packing. 


        #Creating an empty Tuple
        Tuple1 = ()
        print("Initial empty Tuple: ")
        print (Tuple1)
        
        #Creatting a Tuple 
        #with the use of string
        Tuple1 = ('Geeks', 'For')
        print("\nTuple with the use of String: ")
        print(Tuple1)
        
        # Creating a Tuple with
        # the use of list
        list1 = [1, 2, 4, 5, 6]
        print("\nTuple using List: ")
        print(tuple(list1))
        
        #Creating a Tuple 
        #with the use of built-in function
        Tuple1 = tuple('Geeks')
        print("\nTuple with the use of function: ")
        print(Tuple1)

    #  Creating a Tuple with Mixed Datatypes.

        #Creating a Tuple
        #with Mixed Datatype
        Tuple1 = (5, 'Welcome', 7, 'Geeks')
        print("\nTuple with Mixed Datatypes: ")
        print(Tuple1)
        
        #Creating a Tuple
        #with nested tuples
        Tuple1 = (0, 1, 2, 3)
        Tuple2 = ('python', 'geek')
        Tuple3 = (Tuple1, Tuple2)
        print("\nTuple with nested tuples: ")
        print(Tuple3)
        
        #Creating a Tuple
        #with repetition
        Tuple1 = ('Geeks',) * 3
        print("\nTuple with repetition: ")
        print(Tuple1)
        
        #Creating a Tuple 
        #with the use of loop
        Tuple1 = ('Geeks')
        n = 5
        print("\nTuple with a loop")
        for i in range(int(n)):
            Tuple1 = (Tuple1,)
            print(Tuple1)



# -----------------------------Accessing of Tuple--------------------------
    # Tuples are immutable, and usually, they contain a sequence of heterogeneous elements that are accessed via unpacking 
    # or indexing (or even by attribute in the case of named tuples). 
    # Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

    # Note: In unpacking of tuple number of variables on the left-hand side should be equal to a number of values in given tuple a.


        #Accessing Tuple
        #with Indexing
        Tuple1 = tuple("Geeks")
        print("\nFirst element of Tuple: ")
        print(Tuple1[1])
        
        
        #Tuple unpacking
        Tuple1 = ("Geeks", "For", "Geeks")
        
        #This line unpack 
        #values of Tuple1
        a, b, c = Tuple1
        print("\nValues after unpacking: ")
        print(a)
        print(b)
        print(c)


# -----------------------------Concatenation of Tuple--------------------------
    # Concatenation of tuple is the process of joining two or more Tuples. 
    # Concatenation is done by the use of ‘+’ operator. 
    # Concatenation of tuples is done always from the end of the original tuple. 
    # Other arithmetic operations do not apply on Tuples. 
    # Note- Only the same datatypes can be combined with concatenation, an error arises if a list and a tuple are combined. 

        # Concatenaton of tuples
        Tuple1 = (0, 1, 2, 3)
        Tuple2 = ('Geeks', 'For', 'Geeks')

        Tuple3 = Tuple1 + Tuple2

        # Printing first Tuple
        print("Tuple 1: ")
        print(Tuple1)

        # Printing Second Tuple
        print("\nTuple2: ")
        print(Tuple2)

        # Printing Final Tuple
        print("\nTuples after Concatenaton: ")
        print(Tuple3)

# -----------------------------Slicing of Tuple--------------------------

    # Slicing of a Tuple is done to fetch a specific range or slice of sub-elements from a Tuple. 
    # Slicing can also be done to lists and arrays. 
    # Indexing in a list results to fetching a single element whereas Slicing allows to fetch a set of elements. 
    # Note- Negative Increment values can also be used to reverse the sequence of Tuples 

            # Slicing of a Tuple

        # Slicing of a Tuple
        # with Numbers
        Tuple1 = tuple('GEEKSFORGEEKS')

        # Removing First element
        print("Removal of First Element: ")
        print(Tuple1[1:])

        # Reversing the Tuple 
        print("\nTuple after sequence of Element is reversed: ")
        print(Tuple1[::-1])

        # Printing elements of a Range
        print("\nPrinting elements between Range 4-9: ")
        print(Tuple1[4:9])


# -----------------------------Deleting a Tuple------------------------
    # Tuples are immutable and hence they do not allow deletion of a part of it. 
    # The entire tuple gets deleted by the use of del() method. 

    # Note- Printing of Tuple after deletion results in an Error. 

        # Deleting a Tuple
        
        Tuple1 = (0, 1, 2, 3, 4)
        del Tuple1
        
        print(Tuple1)


