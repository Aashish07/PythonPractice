# Constructors are generally used for instantiating an object.
# The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created.
# In Python the __init__() method is called the constructor and is always called when an object is created.


# Types of constructors :

    # default constructor :
        # The default constructor is simple constructor which doesn’t accept any arguments.
        # It’s definition has only one argument which is a reference to the instance being constructed.
    # parameterized constructor :
        # constructor with parameters is known as parameterized constructor.
        # The parameterized constructor take its first argument as a reference
        #  to the instance being constructed known as self and the rest of the arguments are provided by the programmer.

class GeekforGeeks: 
  
    # default constructor 
    def __init__(self): 
        self.geek = "GeekforGeeks"
  
    # a method for printing data members 
    def print_Geek(self): 
        print(self.geek) 

class Addition: 
    first = 0
    second = 0
    answer = 0
      
    # parameterized constructor 
    def __init__(self, f, s): 
        self.first = f 
        self.second = s 