##############################################################################
## Higher-order function is a function that takes a function as an argument or
## returns a function.
##############################################################################


def operate_on_numbers(operation, x, y):
    return operation(x, y)


# Functions to be passed as arguments
def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def power(x, y):
    return x**y


# Using the higher-order function
result_addition = operate_on_numbers(add, 3, 5)
result_multiplication = operate_on_numbers(multiply, 2, 4)
result_power = operate_on_numbers(power, 2, 3)

print("Addition:", result_addition)  # Output: 8
print("Multiplication:", result_multiplication)  # Output: 8
print("Power:", result_power)  # Output: 8
