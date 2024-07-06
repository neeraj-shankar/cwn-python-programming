"""
Write a function called productOfArray which takes in an array of numbers and returns the product of them all
"""

def product_of_array(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * product_of_array(arr[1:])

result = product_of_array([1,2,3])
print(result)