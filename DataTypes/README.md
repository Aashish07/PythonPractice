(Strings, Lists, Tuples, Iterations)

#### List Methods
Function 	Description
Append() 	Add an element to the end of the list
Extend() 	Add all elements of a list to the another list
Insert() 	Insert an item at the defined index
Remove() 	Removes an item from the list
Pop() 	Removes and returns an element at the given index
Clear() 	Removes all items from the list
Index() 	Returns the index of the first matched item
Count() 	Returns the count of number of items passed as an argument
Sort() 	Sort items in a list in ascending order
Reverse() 	Reverse the order of items in the list
copy() 	Returns a copy of the list


#### Built-in functions with List
Function 	Description
reduce() 	apply a particular function passed in its argument to all of the list elements stores the intermediate result and only returns the final summation value
sum() 	Sums up the numbers in the list
ord() 	Returns an integer representing the Unicode code point of the given Unicode character
cmp() 	This function returns 1, if first list is “greater” than second list
max() 	return maximum element of given list
min() 	return minimum element of given list
all() 	Returns true if all element are true or if list is empty
any() 	return true if any element of the list is true. if list is empty, return false
len() 	Returns length of the list or size of the list
enumerate() 	Returns enumerate object of list
accumulate() 	apply a particular function passed in its argument to all of the list elements returns a list containing the intermediate results
filter() 	tests if each element of a list true or not
map() 	returns a list of the results after applying the given function to each item of a given iterable
lambda() 	This function can have any number of arguments but only one expression, which is evaluated and returned.




### Tuples :-

#### Built-In Methods
Built-in-Method 	Description
index( ) 	find in the tuple and returns the index of the given value where it’s available
count( ) 	returns the frequency of occurrence of a specified value

#### Built-In Functions
Built-in Function 	Description
all() 	Returns true if all element are true or if tuple is empty
any() 	return true if any element of the tuple is true. if tuple is empty, return false
len() 	Returns length of the tuple or size of the tuple
enumerate() 	Returns enumerate object of tuple
max() 	return maximum element of given tuple
min() 	return minimum element of given tuple
sum() 	Sums up the numbers in the tuple
sorted() 	input elements in the tuple and return a new sorted list
tuple() 	Convert an iterable to a tuple.

### set Methods :- 

#### Set Methods
Function 	Description
add() 	Adds an element to a set
remove() 	Removes an element from a set. If the element is not present in the set, raise a KeyError
clear() 	Removes all elements form a set
copy() 	Returns a shallow copy of a set
pop() 	Removes and returns an arbitrary set element. Raise KeyError if the set is empty
update() 	Updates a set with the union of itself and others
union() 	Returns the union of sets in a new set
difference() 	Returns the difference of two or more sets as a new set
difference_update() 	Removes all elements of another set from this set
discard() 	Removes an element from set if it is a member. (Do nothing if the element is not in set)
intersection() 	Returns the intersection of two sets as a new set
intersection_update() 	Updates the set with the intersection of itself and another
isdisjoint() 	Returns True if two sets have a null intersection
issubset() 	Returns True if another set contains this set
issuperset() 	Returns True if this set contains another set
symmetric_difference() 	Returns the symmetric difference of two sets as a new set
symmetric_difference_update() 	Updates a set with the symmetric difference of itself and another


### Dictionary Methods :-

#### Dictionary Methods
Methods 	Description
copy() 	They copy() method returns a shallow copy of the dictionary.
clear() 	The clear() method removes all items from the dictionary.
pop() 	Removes and returns an element from a dictionary having the given key.
popitem() 	Removes the arbitrary key-value pair from the dictionary and returns it as tuple.
get() 	It is a conventional method to access a value for a key.
dictionary_name.values() 	returns a list of all the values available in a given dictionary.
str() 	Produces a printable string representation of a dictionary.
update() 	Adds dictionary dict2’s key-values pairs to dict
setdefault() 	Set dict[key]=default if key is not already in dict
keys() 	Returns list of dictionary dict’s keys
items() 	Returns a list of dict’s (key, value) tuple pairs
has_key() 	Returns true if key in dictionary dict, false otherwise
fromkeys() 	Create a new dictionary with keys from seq and values set to value.
type() 	Returns the type of the passed variable.
cmp() 	Compares elements of both dict.



### Arrays data-types codes:-

Type Code -> C Type -> Python Type -> Min(size) in Bytes

'b' -> signed char -> int -> 1
'B' -> unsigned char -> int -> 1
'u' -> Py_UNICODE -> unicode character -> 2
'h' -> signed short -> int -> 2
'H' -> unsigned short -> int -> 2
'i' -> signed int -> int -> 2
'l' -> unsigned int -> int -> 2
'l' -> signed long -> int -> 4
'L' -> unsigned long -> int -> 4
'q' -> signed long long -> int -> 8
'Q' -> unsigned long long -> int -> 8
'f' -> float -> float -> 4
'd' -> double -> float -> 8
