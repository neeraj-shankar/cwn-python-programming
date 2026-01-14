# Create a dictionary of string name as key and their length as value
fruits = ['apple', 'banana', 'cherry']
fruits_length = {fruit:len(fruit) for fruit in fruits}
print(fruits_length) # {'apple': 5, 'banana': 6, 'cherry': 6}

# Create dictionary from pairs from a list
pairs = [('a', 1), ('b', 2), ('c', 3)]
pairs_dict = {k:v for k, v in pairs}
print(pairs_dict) # {'a': 1, 'b': 2, 'c': 3}

# “Python’s for k, v in iterable uses the iterator protocol and sequence unpacking via 
# UNPACK_SEQUENCE at the bytecode level.”
for k, v in pairs:
    print(k, v) # a 1 and so on


# For a given dictionary, create a new dictionary by squaring the values
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
squared_values = {k: v*v for k, v in original.items()}
print(squared_values) # {'a': 1, 'b': 4, 'c': 9, 'd': 16}

# For a given dictionary, invert (exchange) the values and keys and return result
original = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
inverted = {value:key for key, value in original.items()}
print(inverted) # {'red': 'apple', 'yellow': 'banana', 'purple': 'grape'}
