# Module in Python
-----------------------------------------------------------------------------------------------------------------------
1. A module in Python is a file containing Python code. It can define functions, classes, and variables.
2. Modules allow you to logically organize your Python code by breaking it into separate files. Each file can be a module.
3. You can use the import statement to bring functionalities defined in a module into another module or script.


# Package in Python
-----------------------------------------------------------------------------------------------------------------------
1. A package is a way of organizing related modules into a single directory hierarchy.
2. It typically includes an __init__.py file (which can be empty) to indicate that the directory should be treated as a package.
3. Packages can contain sub-packages and modules, forming a nested structure.

-----------------------------------------------------------
my_package/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
    
-----------------------------------------------------------

In summary, a module is a single file containing Python code, and a package is a way to organize related modules into a 
directory hierarchy. The concept of modules and packages supports code organization, reusability, and maintainability in larger Python projects.



# Operators in Python

### 1. Arithmetic Operators
Arithmetic operators are used to perform mathematical operations.

- `+` (Addition): Adds two operands.
- `-` (Subtraction): Subtracts the second operand from the first.
- `*` (Multiplication): Multiplies two operands.
- `/` (Division): Divides the first operand by the second.
- `%` (Modulus): Returns the remainder of the division.
- `**` (Exponentiation): Raises the first operand to the power of the second.
- `//` (Floor Division): Divides the first operand by the second and returns the largest integer less than or equal to the result.

```python
a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.333...
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 1000
print(a // b) # Floor Division: 3
```

### 2. Comparison Operators
Comparison operators compare the values of two operands and return a boolean result.

- `==` (Equal): Returns `True` if both operands are equal.
- `!=` (Not Equal): Returns `True` if operands are not equal.
- `>` (Greater than): Returns `True` if the left operand is greater than the right.
- `<` (Less than): Returns `True` if the left operand is less than the right.
- `>=` (Greater than or equal to): Returns `True` if the left operand is greater than or equal to the right.
- `<=` (Less than or equal to): Returns `True` if the left operand is less than or equal to the right.

```python
a = 10
b = 3

print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False
```

### 3. Logical Operators
Logical operators are used to combine conditional statements.

- `and`: Returns `True` if both statements are true.
- `or`: Returns `True` if one of the statements is true.
- `not`: Reverses the result, returns `False` if the result is true.

```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

### 4. Bitwise Operators
Bitwise operators perform bit-by-bit operations on integers.

- `&` (AND): Sets each bit to 1 if both bits are 1.
- `|` (OR): Sets each bit to 1 if one of two bits is 1.
- `^` (XOR): Sets each bit to 1 if only one of two bits is 1.
- `~` (NOT): Inverts all the bits.
- `<<` (Zero fill left shift): Shift left by pushing zeros in from the right.
- `>>` (Signed right shift): Shift right by pushing copies of the leftmost bit in from the left.

```python
a = 5   # 0b0101
b = 3   # 0b0011

print(a & b)  # AND: 1 (0b0001)
print(a | b)  # OR: 7 (0b0111)
print(a ^ b)  # XOR: 6 (0b0110)
print(~a)     # NOT: -6 (inverts bits)
print(a << 1) # Left Shift: 10 (0b1010)
print(a >> 1) # Right Shift: 2 (0b0010)
```

### 5. Assignment Operators
Assignment operators are used to assign values to variables.

- `=`: Assigns value.
- `+=`: Adds and assigns.
- `-=`: Subtracts and assigns.
- `*=`: Multiplies and assigns.
- `/=`: Divides and assigns.
- `%=`: Modulus and assigns.
- `**=`: Exponentiation and assigns.
- `//=`: Floor division and assigns.

```python
a = 10
a += 5  # a = a + 5
print(a)  # 15

a -= 3  # a = a - 3
print(a)  # 12

a *= 2  # a = a * 2
print(a)  # 24

a /= 4  # a = a / 4
print(a)  # 6.0

a %= 4  # a = a % 4
print(a)  # 2.0

a **= 3  # a = a ** 3
print(a)  # 8.0

a //= 2  # a = a // 2
print(a)  # 4.0
```

### 6. Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object with the same memory location.

- `is`: Returns `True` if both variables are the same object.
- `is not`: Returns `True` if both variables are not the same object.

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)    # True
print(a is c)    # False
print(a is not c) # True
```

### 7. Membership Operators
Membership operators are used to test if a sequence is presented in an object.

- `in`: Returns `True` if a sequence with the specified value is present in the object.
- `not in`: Returns `True` if a sequence with the specified value is not present in the object.

```python
a = [1, 2, 3, 4, 5]

print(3 in a)       # True
print(6 not in a)   # True
```

## Conditional Statements

- In Python, conditional statements are used to execute different blocks of code based on certain conditions. The primary conditional statements in Python are:

1. **if statement**: The `if` statement is used to execute a block of code if a specified condition is true.

   ```python
   if condition:
       # code to execute if condition is true
   ```

2. **if-else statement**: The `if-else` statement is used to execute one block of code if the condition is true, and another block of code if the condition is false.

   ```python
   if condition:
       # code to execute if condition is true
   else:
       # code to execute if condition is false
   ```

3. **if-elif-else statement**: The `if-elif-else` statement is used to check multiple conditions. It executes the block of code corresponding to the first true condition. If none of the conditions are true, the `else` block is executed.

   ```python
   if condition1:
       # code to execute if condition1 is true
   elif condition2:
       # code to execute if condition2 is true
   elif condition3:
       # code to execute if condition3 is true
   else:
       # code to execute if none of the above conditions are true
   ```

4. **Nested if statements**: You can nest `if` statements within each other to check for multiple levels of conditions.

   ```python
   if condition1:
       # code to execute if condition1 is true
       if condition2:
           # code to execute if condition1 and condition2 are true
   ```

5. **Conditional expressions (ternary operators)**: Python also supports a one-line shorthand for `if-else` statements, known as conditional expressions or ternary operators.

   ```python
   result = value_if_true if condition else value_if_false
   ```

6. **match statement (Python 3.10+)**: The `match` statement, introduced in Python 3.10, is similar to a switch-case statement found in other languages. It allows you to match a value against several possible patterns and execute a block of code based on the first matching pattern.

   ```python
   match value:
       case pattern1:
           # code to execute if value matches pattern1
       case pattern2:
           # code to execute if value matches pattern2
       case _:
           # code to execute if none of the above patterns match (default case)
   ```

These conditional statements allow you to control the flow of your Python program by making decisions and executing different code based on varying conditions.

## Flow Control

### Python provides several looping techniques that allow you to iterate over items in a sequence (such as a list, tuple, dictionary, set, or string), execute a block of code multiple times, or create an iterator that generates a sequence of values. Here are the primary looping techniques available in Python:

1. **for loop**: Used to iterate over the elements of a sequence. It's commonly used with the `range()` function or to loop directly over iterable objects like lists, tuples, dictionaries, sets, and strings.

   ```python
   for element in iterable:
       # code block to execute for each element
   ```

2. **while loop**: Executes a block of code as long as a specified condition is true.

   ```python
   while condition:
       # code block to execute while the condition is true
   ```

3. **List comprehensions**: Provide a concise way to create lists. It consists of brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses.

   ```python
   [expression for item in iterable if condition]
   ```

4. **Dictionary comprehensions**: Similar to list comprehensions but for creating dictionaries.

   ```python
   {key_expression: value_expression for item in iterable if condition}
   ```

5. **Set comprehensions**: Similar to list comprehensions but for creating sets.

   ```python
   {expression for item in iterable if condition}
   ```

6. **Generator expressions**: Similar to list comprehensions but for creating generators, which are lazily evaluated.

   ```python
   (expression for item in iterable if condition)
   ```

7. **Nested loops**: You can use one loop inside another loop to iterate over multi-dimensional sequences.

   ```python
   for element1 in iterable1:
       for element2 in iterable2:
           # code block to execute
   ```

8. **Loop control statements**: These are used to modify the behavior of loops.
   - **break**: Terminates the loop and transfers execution to the statement immediately following the loop.
   - **continue**: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
   - **pass**: Acts as a placeholder and does nothing; it's used when a statement is syntactically required but no action is needed.

9. **Itertools module**: Provides a collection of tools for handling iterators. Tools like `cycle`, `count`, `chain`, and `combinations` can be used to create complex iterators.

10. **enumerate()**: Adds a counter to an iterable and returns it as an enumerate object, which can be used directly in for loops.

    ```python
    for index, element in enumerate(iterable, start=0):
        # code block to execute
    ```

11. **zip()**: Takes iterables (can be zero or more), aggregates them in a tuple, and returns it.

    ```python
    for item1, item2 in zip(iterable1, iterable2):
        # code block to execute
    ```

These looping techniques can be combined and used in various ways to achieve the desired iteration behavior in your Python programs.

# Python Tuple Guide

This README provides an overview of tuples in Python, including their characteristics, creation, and various operations that can be performed on them.

## What is a Tuple in Python?

A tuple in Python is a collection of objects separated by commas. Tuples are similar to lists in terms of indexing, nested objects, and repetition. However, the key difference is that tuples are immutable, meaning they cannot be changed after creation, unlike mutable lists.

**Note:** When creating a tuple with a single element, remember to add a comma after the element.

## Tuple Constructor in Python

To create a tuple using the tuple constructor, pass the elements as parameters.

**Example:**
```python
tuple_constructor = tuple(("DSA", "development", "deep learning"))
```

## Immutability in Tuples

Tuples are immutable, ordered, and allow duplicate values. Here are some characteristics of tuples in Python:

1. Items can be found in a tuple without altering it.
2. Items cannot be added to a tuple after it is created.
3. Tuples cannot be appended or extended.
4. Items cannot be removed from a tuple once it is created.

## Operations on Tuples

### 1. Accessing Using Positive and Negative Indexing

```python
animal_list = ("Tiger", "Lion", "Zebra")
positive_index = animal_list[0]  # Access using positive index
negative_index = animal_list[-1] # Access using negative index
```

### 2. Concatenation of Python Tuples

```python
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
tuple3 = tuple1 + tuple2
# Output: (0, 1, 2, 3, 'python', 'geek')
```

### 3. Nesting of Python Tuples

```python
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
nested_tuple = (tuple1, tuple2)
# Output: ((0, 1, 2, 3), ('python', 'geek'))
```

### 4. Repetition of Python Tuples

```python
repeated_tuple = ('python',) * 3
# Output: ('python', 'python', 'python')
```

### 5. Slicing Tuples in Python

Slicing a tuple creates smaller tuples from the original tuple using indexing.

### 6. Deleting a Tuple in Python

While individual elements of a tuple cannot be deleted, the entire tuple can be deleted using the `del` keyword.

**Example:**
```python
del tuple3  # Deletes the entire tuple
# Results in NameError if tuple3 is accessed afterward
```

### 7. Finding the Length of a Python Tuple

The length of a tuple can be determined using the `len()` function.

### 8. Multiple Data Types Within a Tuple

Tuples can contain elements of multiple data types, making them heterogeneous.

### 9. Converting a List to a Tuple

A list can be converted to a tuple using the `tuple()` constructor.

**Example:**
```python
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
```

---

Tuples are a fundamental data structure in Python that provide a way to store a collection of immutable objects. They are particularly useful when you need to ensure that data remains unchanged and when you want to use collections as dictionary keys. Use this guide as a reference for working with tuples in your Python projects.



# Python List Guide

This README provides an overview of lists in Python, including how to create, access, modify, and perform various operations on them.

## What is a List in Python?

A list in Python is a collection of items that can contain elements of different data types, including integers, strings, and objects. Lists are enclosed in square brackets `[]` and the elements are separated by commas. They are mutable, meaning that their contents can be altered after creation.

## Operations on Lists

### 1. Creating a List

```python
my_list = []
animal_list = ["Tiger", "Lion"]
```

**Complexities for Creating a List:**
- Time Complexity: O(1)
- Space Complexity: O(n)

### 2. Creating a List with Multiple Elements

Lists can contain duplicate values with distinct positions, allowing for multiple distinct or duplicate values to be passed as a sequence at the time of list creation.

### 3. Accessing Elements from the List

Elements can be accessed using the index operator `[]`. Nested lists can be accessed using nested indexing.

### 4. Negative Indexing

Negative indexing allows access to elements from the end of the list, with `-1` referring to the last item, `-2` to the second-last, and so on.

**Complexities for Negative Indexing:**
- Time Complexity: O(1)
- Space Complexity: O(1)

### 5. Taking Input for a List

```python
# Input the list as a string
words = input("Enter elements (Space-Separated): ")
# Split the string and store it in a list
lst = words.split()
```

### 6. Adding Elements to a Python List

#### Using `append()` Method

- Adds a single element at a time to the end of the list.
- Tuples can be added since they are immutable.
- Lists can be appended to an existing list.

**Complexities for `append()`:**
- Time Complexity: Amortized O(1)
- Space Complexity: O(1)

#### Using `extend()` Method

- Adds multiple elements at the end of the list.

**Complexities for `extend()`:**
- Time Complexity: O(k), where k is the length of the iterable being extended.
- Space Complexity: O(k), where k is the length of the iterable being extended.

### Reversing a List

#### Using `reverse()` Method

```python
mylist = [1, 2, 3, 4, 5]
mylist.reverse()
```

#### Using `reversed()` Function

```python
my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
```

### Removing Elements from the List

#### Using `remove()` Method

- Removes a specified item from the list.
- Only removes the first occurrence of the element.

**Complexities for `remove()`:**
- Time Complexity: O(n)
- Space Complexity: O(1)

#### Using `pop()` Method

- Removes and returns an element from the list.
- By default, it removes the last element unless an index is specified.

### Slicing of a List

- To print elements from the beginning to a range: `[:index]`
- To print elements from the end: `[:-index]`
- To print elements from a specific index to the end: `[index:]`
- To print the whole list in reverse order: `[::-1]`

### List Comprehension

List comprehensions are a concise way to create new lists by applying an expression to each element of an iterable.

**Example:**

```python
newList = [expression(element) for element in oldList if condition]
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
```

---

Lists are one of the most versatile data structures in Python, allowing for efficient storage and manipulation of sequence data. Use this guide as a reference for working with lists in your Python projects.



# Dictionary in Python

## What is a Dictionary in Python?

A dictionary in Python is a collection of key-value pairs. It is similar to a map and is used to store data values. Unlike other data types that hold only a single value as an element, dictionaries can store multiple data values.

## Creating a Dictionary

### Basic Creation
- A dictionary can be created by placing a sequence of elements within curly braces `{}`, separated by commas.
- Keys must be unique and immutable, while values can be of any data type and can be duplicated.
- Dictionary keys are case sensitive.

### Using `dict()` Function
- A dictionary can also be created using the built-in `dict()` function.
- An empty dictionary is created by using an empty pair of curly braces `{}`.

**Example:**
```python
example_dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
```

## Adding Elements to a Dictionary

### Single Value Addition
- Add one value at a time by assigning a value to a key, e.g., `Dict[Key] = 'Value'`.Nested Key Values


### Updating Existing Value
- Use the `update()` method to update an existing value.

### Nested Key Values
- Nested key values can be added to an existing dictionary.

**Complexities:**
- Time complexity: O(1) for best case, O(n) for worst case
- Space complexity: O(1)

## Accessing Elements of a Dictionary

### Using Keys
- Access items by referring to their key name inside square brackets.

### Using `get()` Method
- Use the `get()` method to access the element, which returns the value for the specified key.

**Example:**
```python
value = dictionary_name.get(key)
```

## Deleting Elements Using `del` Keyword

- Use the `del` keyword to delete items with a specific key.

**Example:**
```python
del dictionary_name[key]
```

## Dictionary Methods

| Method | Description |
| ------ | ----------- |
| `dict.clear()` | Remove all elements from the dictionary |
| `dict.copy()` | Returns a copy of the dictionary |
| `dict.get(key, default=None)` | Returns the value of the specified key |
| `dict.items()` | Returns a list containing a tuple for each key-value pair |
| `dict.keys()` | Returns a list containing the dictionary's keys |
| `dict.update(dict2)` | Updates the dictionary with specified key-value pairs |
| `dict.values()` | Returns a list of all the values in the dictionary |
| `pop(key)` | Removes the element with the specified key |
| `popitem()` | Removes the last inserted key-value pair |
| `dict.setdefault(key, default=None)` | Sets the key to the default value if the key is not in the dictionary |
| `dict.has_key(key)` | Returns true if the dictionary contains the specified key (deprecated in Python 3.x) |

---

Use this guide as a reference for working with dictionaries in Python. Remember that dictionaries are versatile and can be used to represent complex data structures by combining them with other data types.

## More in Dictionaries
- In Python, dictionaries themselves are mutable, which means you can change them after they are created. You can add new key-value pairs, update existing ones, or delete them. However, the keys used within a dictionary must be of immutable types, such as strings, numbers, or tuples that contain only immutable elements. This immutability of keys is necessary because it allows Python to perform efficient hashing to quickly locate key-value pairs.



