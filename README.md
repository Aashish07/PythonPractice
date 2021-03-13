# PythonPractice

1. Python was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code. 

## Variables 

#### In other programming languages like C, C++, and Java, you will need to declare the type of variables but in Python you don’t need to do that. Just type in the variable and when values will be given to it, then it will automatically know whether the value given would be an int, float, or char or even a String.

Python program to declare variables :-
myNumber = 3
print(myNumber) 


## DataStructure

#### List is the most basic Data Structure in python. List is a mutable data structure i.e items can be added to list later after the list creation. It’s like you are going to shop at the local market and made a list of some items and later on you can add more and more items to the list. append() function is used to add data to the list.

Python program to illustrate a list :-
  
1. creates a empty list :-

        nums = []  
  
2. appending data in list :-

        nums.append(21)
        nums.append(40.5)
        nums.append("String")
        print(nums) 

## Input and Output

name = input("Enter your name: ")  

## Selection

#### Selection in Python is made using the two keywords ‘if’ and ‘elif’ and else (elseif)

num1 = 34

    if(num1>12): 

        print("Num1 is good") 

    elif(num1>35): 

        print("Num2 is not gooooo....") 

    else: 

        print("Num2 is great") 

## Functions

#### You can think of functions like a bunch of code that is intended to do a particular task in the whole Python script. Python used the keyword ‘def’ to define a function.

def hello(): 

    print("hello") 
    print("hello again") 

hello() 

#### Now as we know any program starts from a ‘main’ function…lets create a main function like in many other programming languages.
def getInteger(): 

    result = int(input("Enter integer: ")) 
    return result 
  
def Main(): 

    print("Started") 
      
    print(output) 
  
if __name__=="__main__": 
    Main() 

## Iteration (Looping)
As the name suggests it calls repeating things again and again. We will use the most popular ‘for’ loop here.
for step in range(5):

    print(step) 

## Modules

#### Python has a very rich module library that has several functions to do many tasks. ‘import’ keyword is used to import a particular module into your python code.

import math 
  
def Main(): 
    num = -85
  
    # fabs is used to get the absolute  
    # value of a decimal 
    num = math.fabs(num)  
    print(num) 
      
      
if __name__=="__main__": 
    Main() 