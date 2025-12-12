##############################################################################
##  reduce function: a function in the functools module that is used to
##  cumulatively apply a binary function to the items of an iterable, from
##  left to right, so as to reduce the iterable to a single accumulated value
##  Syntax: functools.reduce(function, iterable, initializer=None)

##  function: The binary function that takes two arguments.
##  iterable: The sequence of elements to be reduced.
##  initializer: An optional initial value. If provided, the function will be
##  applied with this value and the first item in the iterable.
##############################################################################
from functools import reduce

# Example: Summing all elements in a list
numbers = [1, 2, 3, 4, 5]

sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # 15


def demontrate_reduce(x, y, z=10):
    return x + y


second_sum = reduce(demontrate_reduce, numbers)
print(f"Custom Sum Result: {second_sum}")  # Custom Sum Result: 15

##############################################################################
## lambda function: Lambda functions are often used for short-term operations
## where a full function definition is unnecessary
## Syntax: lambda arguments: expression
##############################################################################

# Simple example to add two numbers
add = lambda x, y: x + y
result = add(3, 5)
print(f"Total Sum: {result}")  # Total Sum: 8

# Sorting a List of Tuples by the Second Element
students = [('Alice', 25), ('Bob', 20), ('Charlie', 22), ('David', 18)]

# Sort by the second element (age)
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
