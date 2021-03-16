# Inheritance is the capability of one class to derive or inherit the properties from another class. The benefits of inheritance are: 

    # 1. It represents real-world relationships well.
    # 2. It provides reusability of a code. We don’t have to write the same code again and again. 
        # Also, it allows us to add more features to a class without modifying it.
    # 3. It is transitive in nature, which means that if class B inherits from another class A, 
        # then all the subclasses of B would automatically inherit from class A.


        # A Python program to demonstrate inheritance 

# Base or Super class. Note object in bracket. 
# (Generally, object is made ancestor of all classes) 
# In Python 3.x "class Person" is 
# equivalent to "class Person(object)" 
class Person(object): 
	
	# Constructor 
	def __init__(self, name): 
		self.name = name 

	# To get name 
	def getName(self): 
		return self.name 

	# To check if this person is an employee 
	def isEmployee(self): 
		return False


# Inherited or Subclass (Note Person in bracket) 
class Employee(Person): 

	# Here we return true 
	def isEmployee(self): 
		return True

# Driver code 
emp = Person("Geek1") # An Object of Person 
print(emp.getName(), emp.isEmployee()) 

emp = Employee("Geek2") # An Object of Employee 
print(emp.getName(), emp.isEmployee()) 



# Like Java Object class, in Python (from version 3.x), object is root of all classes. 
# Different forms of Inheritance: 
    # 1. Single inheritance: When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.
    # 2. Multiple inheritance: When a child class inherits from multiple parent classes, it is called multiple inheritance. 
        # Unlike Java and like C++, Python supports multiple inheritance. We specify all parent classes as a comma-separated list in the bracket. 
    # 3. Multilevel inheritance: When we have a child and grandchild relationship.
    # 4. Hierarchical inheritance More than one derived classes are created from a single base.
    # 5. Hybrid inheritance: This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.

# Private members of parent class 
    # We don’t always want the instance variables of the parent class to be inherited by the child class 
    # i.e. we can make some of the instance variables of the parent class private, which won’t be available to the child class. 
    # We can make an instance variable by adding double underscores before its name. For example,

    # Python program to demonstrate private members 
# of the parent class 
class C(object): 
	def __init__(self): 
			self.c = 21

			# d is private instance variable 
			self.__d = 42	
class D(C): 
	def __init__(self): 
			self.e = 84
			C.__init__(self) 
object1 = D() 

# produces an error as d is private instance variable 
print(object1.d)					 
