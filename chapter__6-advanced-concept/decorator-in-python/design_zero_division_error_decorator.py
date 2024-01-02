"""
A simple python program to create zero division error decorator
"""


def handle_division_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ZeroDivisionError:
            print("Error: Division by zero!")
    return wrapper


# Applying the decorator to a function
@handle_division_error
def divide(a, b):
    return a / b


# Test the decorated function
print(divide(10, 2))  # Output: 5.0
print(divide(5, 0))   # Output: Error: Division by zero!

