"""
Understanding the behavior and use case of floor() method and ceil() method
"""
import math

# input number values for testing
a = 12.189
b = 3.4536

# Using the floor() to get the value after flooring
# Time Complexity- O(1) and Space Complexity - O(1)
print(f"The greatest integer smaller than the given integer --> {math.floor(b)}")

# Using the ceil() to print value after ceiling
# Time Complexity- O(1) and Space Complexity - O(1)
print(f"The least integer greater than the given number --> {math.ceil(b)}")

# Using the trunc() to print the only integer part
# Time Complexity- O(1) and Space Complexity - O(1)
print(f"The Integer part of the given number --> {math.trunc(b)}")
