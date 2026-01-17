# Decorators in Python
Decorators are Python's way to dynamically alter or extend the behavior of functions or methods without modifying their source code. They are often used for tasks such as logging, enforcing access control, memoization, and more.

## Mental Model
```sql
function → object
decorator → returns new function object
attributes → live on the returned object
```
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

## FAQs

### 1. What is the primary difference between a 'decorator' and a 'decorator factory'?
- A decorator factory is a function that returns a decorator, allowing it to accept configuration arguments.
- Factories add a level of indirection so that arguments can be passed before the actual function wrapping occurs.

### 2. When using a class as a decorator for a method, what is a common issue encountered regarding the 'self' argument?
- The instance of the class being decorated is not passed to the call method of the decorator class
- Class-based decorators often fail to act as descriptors, causing the 'self' of the decorated method to be lost.

### 3. Which method must you implement to make a class-based decorator work correctly as a 'descriptor' for methods?
- The `get` method allows the decorator to return a bound version of the method including the instance ('self').

### 4. In a nested decorator scenario, which decorator has direct access to the original function object?
- The one immediately above the function definition. The bottom-most decorator is the first to receive the original function; others receive the wrapper from below.

### 5. How can you implement a decorator that can be used both with and without arguments (e.g., @dec or @dec(arg))?
- By checking if the first argument is a callable and returning a wrapper or a partial function accordingly.
- Determining if the input is the function to be decorated or a configuration argument allows for flexible usage.

### 6. If multiple decorators are used, which part of the code executes first during the actual call of the decorated function?
- When calling the function, you trigger the outermost (topmost) wrapper first.

### 7. What happens if a decorator adds an attribute to the function object it wraps?
- When a decorator adds attributes, those attributes are attached to the wrapper function it returns. Since the original function is replaced, accessing those attributes works transparently, provided `functools.wraps` is used to preserve metadata.
- This pattern is commonly used for routing, authentication, instrumentation, and configuration in frameworks.

### 8. How would you implement a decorator that validates the types of arguments passed to a function?
- By inspecting *args and **kwargs inside the wrapper and comparing them against expected types.
- The wrapper intercepts the call, allowing it to verify arguments before passing them to the original function.

### 9. Why might you use a decorator to implement a 'Singleton' pattern for a class?
- The decorator can intercept the class call to ensure only one instance is ever created and returned.

### 10. Which attribute, added by @functools.wraps, allows you to access the original, undecorated function?
- `wrapped`: This attribute points back to the original function, allowing you to 'bypass' the decorator if needed.

### 11. How does a 'stateful' closure-based decorator maintain data between function calls?
- By defining a variable in the outer decorator function that the inner wrapper accesses. The closure 'closes over' the local variables of the outer function, keeping them alive across calls.

### 12. Which of these is a valid use for a Class Decorator?
- Class decorators can modify the class object before it is used to create instances.

### 13. What is the purpose of the nonlocal keyword in a stateful decorator?
- To allow the wrapper function to modify a variable defined in the outer decorator function.
- Without nonlocal, the wrapper would create a local variable instead of updating the outer state variable.

### 14. Can you apply a decorator to a lambda function?
- Yes, by passing the lambda as an argument to the decorator function manually.

### 15. What does it mean for a decorator to be 'transparent'?
- It preserves the original function's signature, metadata, and return value behavior.
- A transparent decorator adds functionality (like logging) without changing how the function is used by other code.