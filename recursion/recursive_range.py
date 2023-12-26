"""
Write a function called recursiveRange which accepts a number and adds up all the numbers 
from 0 to the number passed to the function.
"""

def recursive_range(n):
    assert int(n) == n, "The Number must be positive Integer only"
    if n == 0:
        return 0
    return n + recursive_range(n-1)

result = recursive_range(10)
print(result)