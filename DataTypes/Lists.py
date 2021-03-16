# Lists in Python 
# Lists are one of the most powerful tools in python. 
# They are just like the arrays declared in other languages. 
# But the most powerful thing is that list need not be always homogeneous. 
# A single list can contain strings, integers, as well as objects. 
# Lists can also be used for implementing stacks and queues. 
# Lists are mutable, i.e., they can be altered once declared.


# Declaring a list 
    L = [1, "a" , "string" , 1+2] 
    print L 
    L.append(6) 
    print L 
    L.pop() 
    print L 
    print L[1] 


# Output :-
    [1, 'a', 'string', 3]
    [1, 'a', 'string', 3, 6]
    [1, 'a', 'string', 3]
    a


# Lists are just like dynamic sized arrays, declared in other languages (vector in C++ and ArrayList in Java).
#  Lists need not be homogeneous always which makes it a most powerful tool in Python. 
# A single list may contain DataTypes like Integers, Strings, as well as Objects. 
# Lists are mutable, and hence, they can be altered even after their creation.


# ----------------------------Creating List ------------------------------------

    # Lists in Python can be created by just placing the sequence inside the square brackets[]. 
    # Unlike Sets, list doesn’t need a built-in function for creation of list. 

    # Creating a List 
        List = [] 
        print("Blank List: ") 
        print(List) 
        
        # Creating a List of numbers 
        List = [10, 20, 14] 
        print("\nList of numbers: ") 
        print(List) 
        
        # Creating a List of strings and accessing 
        # using index 
        List = ["Geeks", "For", "Geeks"] 
        print("\nList Items: ") 
        print(List[0])  
        print(List[2]) 
        
        # Creating a Multi-Dimensional List 
        # (By Nesting a list inside a List) 
        List = [['Geeks', 'For'] , ['Geeks']] 
        print("\nMulti-Dimensional List: ") 
        print(List) 

    # Creating a list with multiple distinct or duplicate elements

    # A list may contain duplicate values with their distinct positions and 
    # hence, multiple distinct or duplicate values can be passed as a sequence at the time of list creation.


        # Creating a List with  
        # the use of Numbers 
        # (Having duplicate values) 
        List = [1, 2, 4, 4, 3, 3, 3, 6, 5] 
        print("\nList with the use of Numbers: ") 
        print(List) 
        
        # Creating a List with  
        # mixed type of values 
        # (Having numbers and strings) 
        List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks'] 
        print("\nList with the use of Mixed Values: ") 
        print(List) 

        # for size
        len(list1)

    # Adding elements to the list

    # Elements can be added to the List by using built-in append() function. 
    # Only one element at a time can be added to the list by using append() method, 
    # for addition of multiple elements with the append() method, loops are used. 
    # Tuples can also be added to the List with the use of append method because tuples are immutable. 
    # Unlike Sets, Lists can also be added to the existing list with the use of append() method.


        # Creating a List 
        List = [] 
        print("Initial blank List: ") 
        print(List) 
        
        # Addition of Elements  
        # in the List 
        List.append(1) 
        List.append(2) 
        List.append(4) 

    #  ---> Using insert() method

        # append() method only works for addition of elements at the end of the List, 
        # for addition of element at the desired position, insert() method is used. 
        # Unlike append() which takes only one argument, insert() method requires two arguments(position, value). 

                # Creating a List 
        List = [1,2,3,4] 
        print("Initial List: ") 
        print(List) 
        
        # Addition of Element at  
        # specific Position 
        # (using Insert Method) 
        List.insert(3, 12) 
        List.insert(0, 'Geeks') 
        print("\nList after performing Insert Operation: ") 
        print(List) 

    #  ---> Using extend() method
        #Other than append() and insert() methods, there’s one more method for Addition of elements, extend(), 
        # this method is used to add multiple elements at the same time at the end of the list. 

        # Creating a List 
        List = [1,2,3,4] 
        print("Initial List: ") 
        print(List) 
        
        # Addition of multiple elements 
        # to the List at the end 
        # (using Extend Method) 
        List.extend([8, 'Geeks', 'Always']) 
        print("\nList after performing Extend Operation: ") 
        print(List) 



# ----------------------------Removing elements from the List ------------------------------------


    # Using remove() method

        # Elements can be removed from the List by using built-in remove() function but 
        # an Error arises if element doesn’t exist in the set. 
        # Remove() method only removes one element at a time, to remove range of elements, iterator is used. 
        # The remove() method removes the specified item.

        # Note – Remove method in List will only remove the first occurrence of the searched element.

        # Creating a List 
        List = [1, 2, 3, 4, 5, 6,  
                7, 8, 9, 10, 11, 12] 
        print("Intial List: ") 
        print(List) 
        
        # Removing elements from List 
        # using Remove() method 
        List.remove(5) 
        List.remove(6) 
        print("\nList after Removal of two elements: ") 
        print(List) 
        
        # Removing elements from List 
        # using iterator method 
        for i in range(1, 5): 
            List.remove(i) 
        print("\nList after Removing a range of elements: ") 
        print(List) 

    #  Using pop() method :-
        removes last element
        # Removing element at a  
        # specific location from the  
        # Set using the pop() method 
        List.pop(2) 


# ----------------------------Slicing List ------------------------------------

    # In Python List, there are multiple ways to print the whole List with all the elements, 
    # but to print a specific range of elements from the list, we use Slice operation. 
    # Slice operation is performed on Lists with the use of a colon(:). 
    # To print elements from beginning to a range use [: Index], to print elements from end-use [:-Index], 
    # to print elements from specific Index till the end use [Index:], 
    # to print elements within a range, use [Start Index:End Index] and to print the whole List with the use of slicing operation, 
    # use [:]. Further, to print the whole List in reverse order, use [::-1].

        # Creating a List 
        List = ['G','E','E','K','S','F', 
                'O','R','G','E','E','K','S'] 
        print("Intial List: ") 
        print(List) 
        
        # Print elements of a range 
        # using Slice operation 
        Sliced_List = List[3:8] 
        print("\nSlicing elements in a range 3-8: ") 
        print(Sliced_List) 
        
        # Print elements from a  
        # pre-defined point to end 
        Sliced_List = List[5:] 
        print("\nElements sliced from 5th "
            "element till the end: ") 
        print(Sliced_List) 
        
        # Printing elements from 
        # beginning till end 
        Sliced_List = List[:] 
        print("\nPrinting all elements using slice operation: ") 
        print(Sliced_List) 

