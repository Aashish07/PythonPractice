# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
# It describes the idea of wrapping data and the methods that work on data within one unit. 
# This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
# To prevent accidental change, an object’s variable can only be changed by an object’s method. 
# Those types of variables are known as private variable.


# --Protected members -->>
    # those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. 
    # To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.
    # Python program to
# demonstrate protected members

# Creating a base class
class Base:
    def __init__(self):
		# Protected member
		self._a = 2

# --Private members ----->>
    # Private members are similar to protected members, 
    # the difference is that the class members declared private should neither be accessed outside the class nor by any base class. 
    # to define a private member prefix the member name with double underscore “__”.

# Creating a base class
class Base:
    def __init__(self):
		# Private member
		self.__a = 2