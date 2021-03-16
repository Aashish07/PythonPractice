# Python Classes and Objects
    # Class creates a user-defined data structure, which holds its own data members and member functions, 
    # which can be accessed and used by creating an instance of that class. 
    # A class is like a blueprint for an object.

# Some points on Python class:  

    # Classes are created by keyword class.
    # Attributes are the variables that belong to a class.
    # Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute

    #     Class Definition Syntax:

    # class ClassName:
    #     # Statement-1
    #     .
    #     .
    #     .
    #     # Statement-N

# ---------------------------- Class Objects ----------------------------------

    # An Object is an instance of a Class. 
    # A class is like a blueprint while an instance is a copy of the class with actual values.
    # An object consists of : 

    #     State: It is represented by the attributes of an object. It also reflects the properties of an object.
    #     Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
    #     Identity: It gives a unique name to an object and enables one object to interact with other objects.

            # # Python3 program to
            # # demonstrate instantiating
            # # a class


            # class Dog: 
                
            #     # A simple class
            #     # attribute
            #     attr1 = "mammal"
            #     attr2 = "dog"

            #     # A sample method 
            #     def fun(self): 
            #         print("I'm a", self.attr1)
            #         print("I'm a", self.attr2)

            # # Driver code
            # # Object instantiation
            # Rodger = Dog()

            # # Accessing class attributes
            # # and method through objects
            # print(Rodger.attr1)
            # Rodger.fun()

# this  - java
# self - python 

# --------------------------- __init__method --------------------------------------

    # The __init__ method is similar to constructors in C++ and Java. 
    # Constructors are used to initializing the object’s state. 
    # Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. 

            # A Sample class with init method 
        class Person: 

            # init method or constructor 
            def __init__(self, name): 
                self.name = name 

            # Sample Method 
            def say_hi(self): 
                print('Hello, my name is', self.name) 

        p = Person('Nikhil') 
        p.say_hi() 

# ----------------------- Class and Instance Variables ------------------------------

    # Instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class. 
    # Instance variables are variables whose value is assigned inside a constructor or method with self 
    # whereas class variables are variables whose value is assigned in the class.

    



