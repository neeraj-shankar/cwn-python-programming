Function Overview
-----------------------------------------------------------------------------------------------------------------------
In Python, a function is treated as a first-class object. This means that a function has all the rights as any other 
variable in the language.

That's why, we can assign a function to a variable, pass it to a function or return it from a function. Just like any 
other variable.


What is map() function ?
-----------------------------------------------------------------------------------------------------------------------
map() function returns a map object(which is an iterator) of the results after applying the given function to each item
of a given iterable (list, tuple etc.)
Syntax --> map(function, iter)


Zip Function
-----------------------------------------------------------------------------------------------------------------------
1. The zip function in Python is used to combine two or more iterables (e.g., lists, tuples) element-wise.
2. Returns the zip object after combining corresponding items both iterables as tuple. 
3. When using the zip function with iterables of different lengths, the resulting iterator will have as many elements 
   as the shortest iterable. The excess elements from the longer iterables will be ignored.

Syntax: zip(iterable1, iterable2, ...)


About reduce
------------------------------------------------------------------------------------------------------------------
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements
mentioned in the sequence passed along.This function is defined in “functools” module.

example -->
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
output --> 15
