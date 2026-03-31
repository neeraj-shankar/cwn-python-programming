# Functions and Methods

## Functions vs. Methods: The Python Way
In Python, everything is an object—including functions.

- **Function:** A block of code defined globally or within a module using def. It stands alone and is called by its name.

- **Method:** A *function that is "bound" to an object*. It is defined inside a class and (usually) takes self as its first argument to access the object's data.

```python
# A Function
def greet(name):
    return f"Hello, {name}"

# A Method
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self): # 'self' makes this a method
        return f"Hello, {self.name}"
```

### Python vs. Java: The Philosophy Shift

### Note:
- Here is a "brain-melt" moment for Python learners: A method is just a function that automatically passes the object instance as the first argument.

```python
p = Person("Alice")

# These two are exactly the same:
print(p.greet())               # Standard method call
print(Person.greet(p))         # Calling the function from the class and passing 'p' manually
```

## Closures: The "Memory" of a Function
In Python, functions are first-class citizens (you can pass them around like variables). A closure happens when a nested function remembers the variables from its enclosing scope, even after the outer function has finished executing.

For a closure to exist in Python, you must have:
- A nested function (a function inside a function).
- The nested function must refer to a value defined in the enclosing scope.
- The enclosing function must return the nested function.

```python
def make_secret(message):
    # This is the 'enclosing' scope
    def reveal():
        # This is the 'nested' function
        print(f"The secret is: {message}")
    
    return reveal  # Return the function object itself

# 1. We create the closure
my_vault = make_secret("I love Python")

# 2. 'make_secret' has finished executing here. 
# Usually, 'message' would be gone from memory.

# 3. But 'my_vault' still knows it!
my_vault()  # Output: The secret is: I love Python
```
- When reveal is defined, it "closes over" the variable message. Python stores this in a special attribute called `__closure__`.

### The **nonlocal** Keyword
- If you want to modify the variable inside the closure (not just read it), you need the nonlocal keyword.

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count  # Tells Python: "Look in the outer function, not global"
        count += 1
        return count
    return increment

counter_a = make_counter()
print(counter_a()) # 1
print(counter_a()) # 2
```

## Decorators
Closures are the engine inside a Decorator. A decorator is just a closure where the "secret message" being passed in is actually another function.

- So you can say that a decorator is essentially a **closure** that takes a function as an argument and returns a new, "wrapped" version of it. It allows you to add functionality to existing code without permanently modifying it

```python
def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello, world!")

say_hello()
# Output:
# Before the function call
# Hello, world!
# After the function call
```

---

### **3. Breaking Down How Decorators Work**

1. **@ Decorator Syntax** :
   The `@decorator_name` syntax is shorthand for:

```python
   function_name = decorator_name(function_name)
```

1. **Wrapper Functions** :

* The `wrapper` function wraps around the target function.
* It allows you to add functionality before or after calling the original function.

1. **Preserving Metadata with `functools.wraps`** :
   Decorators can obscure the original function's name and docstring. To preserve them, use `functools.wraps`:

```python
   import functools

   def decorator(func):
       @functools.wraps(func)
       def wrapper(*args, **kwargs):
           print(f"Calling {func.__name__}")
           return func(*args, **kwargs)
       return wrapper

   @decorator
   def sample_function():
       """This is a sample function."""
       print("Function body")

   sample_function()
   print(sample_function.__name__)  # Output: sample_function
   print(sample_function.__doc__)   # Output: This is a sample function.
```

---

## The Iterators
In Python, an iterator is an *object* that allows you to traverse through all the elements of a collection, regardless of its specific implementation.

- Think of an Iterable as a book, and an Iterator as a bookmark that keeps track of which page you are on.

### The Iterator Protocol
- To be an iterator in Python, an object must implement *two specific magic* methods:

1. **`__iter__():`** This returns the iterator object itself. It’s required so that you can use the object in for loops.

2. **`__next__():`** This returns the next value from the data stream. If there are no more items, it must raise a StopIteration exception.

### Iterable vs. Iterator
This is a distinction that trips up many developers:

- **Iterable:** Anything you can loop over (List, Tuple, String). It has an __iter__ method that creates a new iterator.
- **Iterator:** The stateful helper that actually does the work. It remembers where it is in the sequence.

## Generators
- A Generator is a function that acts like an *iterator but uses the yield keyword* to simplify everything.

### The `yield` Keyword
When a function contains yield, Python marks it as a special type of function.
- When called, it doesn't run the code immediately. It returns a Generator Object.
- When you call next() on that object, the function runs until it hits yield.
- It "freezes" its state, returns the value, and waits.
- When called again, it resumes exactly where it left off.

### Generator Expressions

```python
# List Comprehension (Eager)
my_list = [i**2 for i in range(1000)] 

# Generator Expression (Lazy)
my_gen = (i**2 for i in range(1000)) 

print(next(my_gen)) # 0
print(next(my_gen)) # 1
```

## The Descriptor Protocol
The Descriptor Protocol is the "secret sauce" behind how Python handles *attributes*, *methods*, *property*, **classmethod**, and **staticmethod**. It is one of the most powerful, low-level features of the language.

- A descriptor is an object that defines how other objects access its attributes.

### 1. The Core Protocol
An object is a descriptor if it defines at least one of these three "magic" methods:
- `__get__(self, obj, type=None)`: Called when the attribute is read.
- ` __set__(self, obj, value)`: Called when the attribute is assigned.
- `__delete__(self, obj)`: Called when the attribute is deleted.


```python
class PositiveNumber:
    def __init__(self):
        self._values = {} # Internal storage

    def __get__(self, instance, owner):
        return self._values.get(instance)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Must be positive!")
        self._values[instance] = value

class Profile:
    age = PositiveNumber() # age is now a descriptor

p = Profile()
p.age = 25  # Calls __set__
# p.age = -5 # Raises ValueError
```

### 2. Why is this important for Decorators?
- When you decorate a method with a class, the decorator replaces the method. But a standard class instance doesn't know how to pass the self of the parent class.
- By adding `__get__` to your decorator class, you turn it into a Descriptor. When someone calls the decorated method, Python triggers `__get__`, giving you a chance to "bind" the instance (self) to the function.

## FAQs

### 1. In a Python closure, what is the purpose of the 'nonlocal' keyword?
- To allow the inner function to modify a variable defined in the enclosing scope.
- Without this keyword, assigning to the variable would create a new local variable instead of modifying the one in the outer function.

### 2. What is a major advantage of using a Generator Expression over a List Comprehension for large datasets?

### 3. What is the primary purpose of using 'functools.wraps' when creating a decorator?
- To preserve the original function's metadata, such as its name and docstring.
- Without this, the decorated function would appear to have the name and docstring of the 'wrapper' function instead.

### 4. In a generator, what does the 'yield from' expression accomplish?
- It delegates part of its operations to another iterable or generator.
- This creates a transparent bridge between the outer generator and a sub-generator, yielding all its values automatically.

### 5. What is a 'Decorator Factory'?
- A function that returns a decorator, allowing the decorator to accept its own arguments.
- This triple-nested structure is necessary when you want to write syntax like @my_decorator(arg).

### 6. If you define a class with a 'call' method, how can it be used in relation to functions?
- It can be used as a stateful decorator. The class instance can store state in 'self' across multiple calls to the decorated function.

### 7. Why would you use a closure instead of a global variable to maintain state?
- Closures provide data encapsulation, preventing the state from being modified by outside code. By 'closing over' a variable, it remains private to that specific function instance.

### 8. What is the result of using a generator expression inside a function that expects a list, like 'sum()'?
- It will execute efficiently without creating an intermediate list in memory.

### 9. What happens if a generator function contains a 'return' statement with a value?
- It stops the generator and attaches the value to the StopIteration exception.

