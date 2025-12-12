## Decorators in Python

Decorators are Python's way to dynamically alter or extend the behavior of functions or methods without modifying their source code. They are often used for tasks such as logging, enforcing access control, memoization, and more.

---

### **2. Anatomy of a Decorator**

A decorator is just a function that takes another function as an argument, does something with it (e.g., wraps it in another function), and returns the result.

Here’s the simplest example:

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

### **4. Practical Use Cases**

#### **4.1. Logging**

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} was called with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b

print(add(3, 5))
# Output:
# Function add was called with (3, 5) and {}
# 8
```

#### **4.2. Access Control**

```python
def require_admin(func):
    def wrapper(user):
        if not user.get("is_admin"):
            raise PermissionError("User must be an admin!")
        return func(user)
    return wrapper

@require_admin
def view_dashboard(user):
    return "Welcome to the admin dashboard."

print(view_dashboard({"is_admin": True}))  # Works
# view_dashboard({"is_admin": False})     # Raises PermissionError
```

#### **4.3. Timing Function Execution**

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished!")

slow_function()
# Output:
# Finished!
# slow_function took 2.00 seconds
```

#### **4.4. Memoization**

```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Output: 55
```

---

### **5. Advanced Topics**

#### **5.1. Decorators with Arguments**

Decorators can accept arguments if they are wrapped in an additional function:

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()
# Output: "Hello!" printed 3 times
```

#### **5.2. Class-based Decorators**

Instead of using a function as a decorator, you can use a class:

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Call {self.calls} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()
say_hello()
# Output:
# Call 1 to say_hello
# Hello!
# Call 2 to say_hello
# Hello!
```

#### **5.3. Chaining Decorators**

Multiple decorators can be applied to a function. They are executed from the bottom up:

```python
def decor1(func):
    def wrapper():
        print("Decor1 Start")
        func()
        print("Decor1 End")
    return wrapper

def decor2(func):
    def wrapper():
        print("Decor2 Start")
        func()
        print("Decor2 End")
    return wrapper

@decor1
@decor2
def show():
    print("Hello from the function!")

show()
# Output:
# Decor1 Start
# Decor2 Start
# Hello from the function!
# Decor2 End
# Decor1 End
```

---

### **6. Challenges to Try**

1. Write a decorator that restricts a function to only accept even numbers as arguments.
2. Create a decorator that retries a function if it raises an exception, with a maximum of 3 retries.
3. Implement a decorator that converts the return value of a function into JSON format.

### FAQs based on Decorators

1. **What is a decorator in Python? Can you explain how it works?**

   - Expect to explain the concept of decorators as functions that modify the behavior of other functions or methods. You should be able to describe the process of wrapping a function and the use of `@` syntax.
2. **Can you write a decorator that times the execution of a function?**

   - This question tests your ability to write practical decorators. You might need to use the `time` module to calculate the duration of function execution.
3. **How can you preserve a function's metadata when using decorators?**

   - Discuss the use of `functools.wraps` and why it's important to preserve a function's `__name__`, `__doc__`, and other attributes.
4. **What is the difference between `@staticmethod`, `@classmethod`, and instance methods?**

   - You should be able to explain the differences and when to use each one.
5. **Can you create a decorator that caches the result of a function call?**

   - This question assesses your understanding of more complex decorator patterns, such as memoization or caching.
6. **How would you implement a decorator that can be used both with and without arguments?**

   - This tests your knowledge of writing decorators that can handle optional arguments, which requires an extra layer of function nesting.
7. **Explain the decorator pattern and its advantages and disadvantages.**

   - Discuss the design pattern, not just the Python feature, and when it might be useful or problematic in software design.
8. **Can you stack multiple decorators on a single function? What is the order of execution?**

   - You should know how to apply multiple decorators to a function and understand how the order affects the result.
9. **How do decorators interact with function arguments?**

   - Explain how to write decorators that can handle functions with any combination of arguments using `*args` and `**kwargs`.
10. **Are there any performance considerations when using decorators?**

    - Discuss any potential performance impacts of decorators, such as added overhead or issues with recursive decorators.
11. **Can you explain how a class-based decorator works compared to a function-based decorator?**

    - You might need to describe how to implement a decorator using a class with `__call__` method and when it might be preferable over a function-based decorator.
12. **How can you debug a function wrapped with a decorator?**

    - Discuss strategies for debugging, such as temporarily disabling the decorator or using tools that understand decorators.
13. **Can you use decorators to enforce function argument types or return types?**

    - This question assesses your knowledge of using decorators for type checking, which can be particularly relevant with the introduction of type hints in Python.
14. **How would you implement a decorator that logs every call to the decorated function?**

    - This tests your ability to write decorators for cross-cutting concerns like logging.
15. **Can you describe a real-world scenario where you successfully used a decorator in your code?**

    - Be prepared to discuss actual use cases from your experience, which might include decorators for authentication, authorization, transaction handling, or other aspects.
