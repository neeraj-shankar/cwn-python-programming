##############################################################################
## Decorators function with parameters:
## Syntax: func = decorator(func)
## where func is the function being decorated and decorator is the function
## used to decorate it.
##############################################################################


def decorator(func):
    def wrapper():
        print(f"This is printed before function is called.")
        func()
        print(f"This is printed after the function is called.")

    return wrapper


def say_hello():
    print(f"Hello! The function is executing")


greet = decorator(say_hello)

greet()  # This is printed before function is called.
# Hello! The function is executing
# This is printed after the function is called.

# Explanation: We passed the say_hello function to the decorator function.
# In effect, the say_hello now points to the wrapper function returned by the
# decorator. However, the wrapper function has a reference to the original
# say_hello() as func, and calls that function between the two calls to print().


##############################################################################
## Syntactic Decorator: Python introduced a new way to use decorators by
## providing syntactic sugar with the @ symbol.
##############################################################################
def decorator(func):
    def wrapper():
        print("This is printed before the function is called")
        func()
        print("This is printed after the function is called")

    return wrapper


@decorator
def say_hello():
    print("Hello! The function is executing")


say_hello()

##############################################################################
## Preserving the Original Name and Docstring of the Decorated Function:
## In Python, functions have a name attribute and a docstring to help with
## debugging and documentation.But, when we decorate a function its identity
## is changed to the wrapper function
##############################################################################


@decorator
def say_hello():
    """This function says hello when called"""
    print(f"Hello! This function is executing.")


print(say_hello.__name__)  # wrapper
help(say_hello)  # Help on function wrapper in module __main__:
# wrapper()

# As the say_hello now points to the wrapper function, it is showing its
# information instead of the original function.

##############################################################################
## To fix this, we need to use another decorator called wraps on the wrapper
## function.
##############################################################################
import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper():
        print("This is printed before the function is called")
        func()
        print("This is printed after the function is called")

    return wrapper


@decorator
def say_hello():
    """This function says hello when called"""
    print("Hello! The function is executing")


print(say_hello.__name__)
help(say_hello)

##############################################################################
## Decorators Functions with Parameters
## What if the function we are decorating has some parameters?
## Example: Decorating a function that takes name as input param and print
## personalized greet.
##############################################################################
import functools


def say_it_twice(func):
    @functools.wraps(func)
    def wrapper():
        func()
        func()

    return wrapper


@say_it_twice
def say_hello(name):
    print(f"Hello, Good Morning: {name}")


# It will return Type Error because the wrapper function we defined inside the
# decorator does not accept any argument.
# say_hello("Neeraj") # TypeError: say_hello() takes 0 positional arguments but 1 was given

##############################################################################
## The Fix: The straightforward way to solve this would be to let the wrapper
## accept one argument, but then we won't be able to use the do_twice decorator
## with a function with more than one argument.
## Use a variable number of parameters in the wrapper function to handle any
## number of arguments in the decorated function.
##############################################################################
import functools


def say_it_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@say_it_twice
def say_hello(name):
    print(f"Hello, Good Morning: {name}")


# calling the hello function
say_hello("Neeraj")  # Hello, Good Morning: Neeraj
# Hello, Good Morning: Neeraj


##############################################################################
## Returning Values from Decorated Functions
## What happens to the returned value from the decorated function?
##############################################################################
def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@do_twice
def add(num1, num2):
    print(f"Adding {num1} and {num2}")
    return num1 + num2


print("The sum is:", add(1, 2))  # The sum is: None
# Explaination: The add function was called twice as expected but we got None
# in the return value. This is because the wrapper function does not return
# any value.

##############################################################################
## The Fix: To fix this, we need to make sure the wrapper function returns the
## return value of the decorated function.
##############################################################################
import functools

def do_twice(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    func(*args, **kwargs)
    return func(*args, **kwargs)
  
  return wrapper

@do_twice
def add(num1, num2):
  print(f"Adding {num1} and {num2}")
  return num1 + num2

print("The sum is:", add(1, 2)) # Adding 1 and 2
# Adding 1 and 2
# The sum is: 3

##############################################################################
## Decorators with Arguments: You can pass arguments to the decorator itself!
## We can define the decorator inside another function that accepts the 
## arguments and then use those arguments inside the decorator. You also need
## to return the decorator from the enclosing function.
#############################################################################
def repeat(num_times):
  def decorator_repeat(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(num_times):
        value = func(*args, **kwargs)
      return value

    return wrapper
  
  return decorator_repeat

@repeat(num_times=3)
def say_hello(name):
  print(f"Hello, {name}!")
  return name

print(f"Given Name: {say_hello("Kitty")}") # Hello, Kitty!
# Hello, Kitty!
# Hello, Kitty!
# Given Name: Kitty

