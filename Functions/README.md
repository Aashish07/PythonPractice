A function in Python is an aggregation of related statements designed to perform a computational, logical, or evaluative task. The idea is to put some commonly or repeatedly done task together and make a function so that instead of writing the same code again and again for different inputs, we can call the function to reuse code contained in it over and over again. 

Functions can be both built-in or user-defined. It helps the program to be concise, non-repetitive, and organized.

Syntax:-
    def function_name(parameters):
    """docstring"""
    statement(s)

Docstring

The first string after the function is called the Document string or Docstring in short. This is used to describe the functionality of the function. The use of docstring in functions is optional but it is considered a good practice.

The below syntax can be used to print out the docstring of a function:

Syntax: print(function_name.__doc__)

### One important thing to note is, in Python every variable name is a reference. When we pass a variable to a function, a new reference to the object is created. Parameter passing in Python is the same as reference passing in Java. 

Variable-length arguments:
    We can have both normal and keyword variable number of arguments. 

Anonymous functions: 

In Python, an anonymous function means that a function is without a name. As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.

Properties of first class functions:

    A function is an instance of the Object type.
    You can store the function in a variable.
    You can pass the function as a parameter to another function.
    You can return the function from a function.
    You can store them in data structures such as hash tables, lists, …

