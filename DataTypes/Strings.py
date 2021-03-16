# Strings in Python 
# A string is a sequence of characters. 
# It can be declared in python by using double-quotes.
#  Strings are immutable, i.e., they cannot be changed.


# Assigning string to a variable 
a = "This is a string"
print (a) 

# In Python, Strings are arrays of bytes representing Unicode characters. 
# However, Python does not have a character data type, a single character is simply a string with a length of 1. 
# Square brackets can be used to access elements of the string.


# Creating a String  
# with single Quotes 
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ") 
print(String1) 
  
# Creating a String 
# with double Quotes 
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ") 
print(String1) 
  
# Creating a String 
# with triple Quotes 
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ") 
print(String1) 
  
# Creating String with triple 
# Quotes allows multiple lines 
String1 = '''Geeks 
            For 
            Life'''
print("\nCreating a multiline String: ") 
print(String1) 


# Printing First character 
print("\nFirst character of String is: ") 
print(String1[0]) 


# ------------ String slicing --------
# To access a range of characters in the String, method of slicing is used. 
# Slicing in a String is done by using a Slicing operator (colon).

# Creating a String 
String1 = "GeeksForGeeks"
print("Initial String: ")  
print(String1) 
  
# Printing 3rd to 12th character 
print("\nSlicing characters from 3-12: ") 
print(String1[3:12]) 
  
# Printing characters between  
# 3rd and 2nd last character 
print("\nSlicing characters between " +
    "3rd and 2nd last character: ") 
print(String1[3:-2]) 


# --------------------Deleting/Updating from a String

# In Python, Updation or deletion of characters from a String is not allowed. 
# This will cause an error because item assignment or item deletion from a String is not supported. 
# Although deletion of entire String is possible with the use of a built-in del keyword. 
# This is because Strings are immutable, hence elements of a String cannot be changed once it has been assigned. 
# Only new strings can be reassigned to the same name.


# ->Updating
    String1 = "Hello, I'm a Geek"
    print("Initial String: ") 
    print(String1) 
    
    # Updating a String 
    String1 = "Welcome to the Geek World"
    print("\nUpdated String: ") 
    print(String1) 

# -> Deleting
    
    
    String1 = "Hello, I'm a Geek"
    print("Initial String: ") 
    print(String1) 
    
    # Deleting a String 
    # with the use of del 
    del String1  
    print("\nDeleting entire String: ") 
    print(String1) 

# -------------------------------Formatting of strings

# Strings in Python can be formatted with the use of format() method which is very versatile and powerful tool for formatting of Strings. 
# Format method in String contains curly braces {} as placeholders which can hold arguments according to position or keyword to specify the order.
  
    # Default order 
    String1 = "{} {} {}".format('Geeks', 'For', 'Life') 
    print("Print String in default order: ") 
    print(String1) 
    
    # Positional Formatting 
    String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life') 
    print("\nPrint String in Positional order: ") 
    print(String1) 
    
    # Keyword Formatting 
    String1 = "{l} {f} {g}".format(g = 'Geeks', f = 'For', l = 'Life') 
    print("\nPrint String in order of Keywords: ") 
    print(String1) 


