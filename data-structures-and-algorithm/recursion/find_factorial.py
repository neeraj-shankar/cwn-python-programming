"""
Python Program to find the factorial of any postive integer
"""

def factorial(num):
    assert int(num) == num, "The Number must be an ineteger"
    if num == 0:
        return 1
    elif num < 0:
        return num * factorial(num+1)
    return num * factorial(num-1)

result = factorial(-2)
print(result)