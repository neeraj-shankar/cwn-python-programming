import time
import re
# Can you write a decorator that times the execution of a function?
import time
from functools import wraps

def calculate_execution_time(func):
    """
    Decorator that calculates the execution time of the decorated function.

    This decorator adds functionality to any function to measure and print the
    time it takes to execute from start to finish.

    Parameters:
    func (callable): The function to be decorated.

    Returns:
    callable: The wrapper function which adds timing behavior to the input function.
    """
    
    # The wrapper function that will replace 'func'
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Record the start time of the function execution
        start_time = time.time()
        
        # Call the original function with its arguments and keyword arguments
        result = func(*args, **kwargs)
        
        # Record the end time of the function execution
        end_time = time.time()
        
        # Calculate the elapsed time by subtracting the start time from the end time
        elapsed_time = end_time - start_time
        
        # Print the name of the function and its execution time
        print(f"{func.__name__} took {elapsed_time} seconds for its execution.")
        print(f"Metadata about original function: {func.__doc__}")
        
        # Return the result of the function call
        return result
    
    # Return the wrapper function to replace the original function
    return wrapper

def cache_decorator(func):
    """
    Decorator that caches the results of the function call.
    The cache is stored in a dictionary where the keys are the arguments
    and keyword arguments passed to the function, and the values are the results
    of the function calls.
    """
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key based on the function's arguments and keyword arguments
        # Since kwargs is a dictionary, we turn it into a tuple of sorted (key, value) pairs
        cache_key = (args, tuple(sorted(kwargs.items())))
        # If the result is already in the cache, return it
        if cache_key in cache:
            return cache[cache_key]

        # Otherwise, call the function and store the result in the cache
        result = func(*args, **kwargs)
        cache[cache_key] = result
        return result

    return wrapper


from functools import wraps, partial

def my_decorator(*args, **kwargs):
    # If the first argument is callable, it means the decorator has been used without arguments
    print(F"Total arguments passed: {args}")
    if len(args) == 1 and callable(args[0]) and not kwargs:
        func = args[0]
        @wraps(func)
        def wrapper(*func_args, **func_kwargs):
            print("Decorator without arguments")
            return func(*func_args, **func_kwargs)
        return wrapper
    else:
        # The decorator has been used with arguments, so we return a new decorator
        def decorator_with_args(func):
            @wraps(func)
            def wrapper(*func_args, **func_kwargs):
                print(f"Decorator with arguments: args={args}, kwargs={kwargs}")
                return func(*func_args, **func_kwargs)
            return wrapper
        return decorator_with_args

# Example usage:

# Used without arguments
@my_decorator
def my_function1():
    print("Function 1 called")

my_function1()

# Used with arguments
@my_decorator(42, debug=True)
def my_function2():
    print("Function 2 called")

my_function2()
