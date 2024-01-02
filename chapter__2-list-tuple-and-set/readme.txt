What is a list in python?
-----------------------------------------------------------------------------------------------------------------------
Python Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and ArrayList in Java).
In simple language, a list is a collection of things, enclosed in [ ] and separated by commas.

A single list may contain DataTypes like Integers, Strings, as well as Objects. Lists are mutable, and hence, they can
be altered even after their creation.


Operations on list
-----------------------------------------------------------------------------------------------------------------------

1. Creating a list
-----------------------------------------------------------
my_list = []
animal_list = ["Tiger", "Lion"]
Complexities for Creating Lists
Time Complexity: O(1) and Space Complexity: O(n)

2. Creating a list with multiple distinct or duplicate elements
-----------------------------------------------------------
A list may contain duplicate values with their distinct positions and hence, multiple distinct or duplicate values can
be passed as a sequence at the time of list creation.

3. Accessing elements from the List
-----------------------------------------------------------
Use the index operator [ ] to access an item in a list. The index must be an integer. Nested lists are accessed using
nested indexing.

4. Negative indexing
----------------------------------------------------------
In Python, negative sequence indexes represent positions from the end of the array.
Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second-last item, etc.
Time Complexity: O(1) and Space Complexity: O(1)

5. Taking Input of a Python List
-----------------------------------------------------------
We can take the input of a list of elements as string, integer, float, etc. But the default one is a string.
# input the list as string
words = input("Enter elements (Space-Separated): ")
# split the strings and store it to a list
lst = words.split()

6. Adding Elements to a Python List
-----------------------------------------------------------
Using append() method -->
-----------------------------
1. Only one element at a time can be added to the list by using the append() method, for the addition of multiple elements
with the append() method, loops are used.
2. Tuples can also be added to the list with the use of the append method because tuples are immutable.
3. Unlike Sets, Lists can also be added to the existing list with the use of the append() method.

Using extend() method
-----------------------------
Other than append() and insert() methods, there’s one more method for the Addition of elements, extend(), this method
is used to add multiple elements at the same time at the end of the list.
Note: append() and extend() methods can only add elements at the end.
Time Complexity: O(n) and Space Complexity: O(1)

Reversing a List
-----------------------------------------------------------
1. A list can be reversed by using the reverse() method in Python.
eg --> mylist = [1, 2, 3, 4, 5]
       mylist.reverse()

2. The reversed() function returns a reverse iterator, which can be converted to a list using the list() function.
eg --> my_list = [1, 2, 3, 4, 5]
       reversed_list = list(reversed(my_list))

Removing Elements from the List
-----------------------------------------------------------
Using remove() method
-----------------------------
1. Elements can be removed from the List by using the built-in remove() function but an Error arises if the element
doesn’t exist in the list.
2. Remove() method only removes one element at a time, to remove a range of elements, the iterator is used.
3. The remove() method removes the specified item.
Note: Remove method in List will only remove the first occurrence of the searched element.
Time Complexity: O(n) and Space Complexity: O(1)

Using pop() method
-----------------------------
pop() function can also be used to remove and return an element from the list, but by default it removes only the last
element of the list, to remove an element from a specific position of the List, the index of the element is passed as
an argument to the pop() method.

Slicing of a List
-----------------------------------------------------------
1. To print elements from beginning to a range use:--> [:index]
2. To print elements from end-use:--> [:-index]
3. To print elements from a specific Index till the end use:--> [index:]
4. To print the whole list in reverse order, use:-->[::-1]

List Comprehension
-----------------------------------------------------------
1. List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc.
2. A list comprehension consists of brackets containing the expression, which is executed for each element along with
   the for loop to iterate over each element.

eg--> newList = [ expression(element) for element in oldList if condition ]
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]



