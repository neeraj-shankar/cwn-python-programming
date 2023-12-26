""" 
Python program to show demonstrate if the array is made of only unique elements.
"""

import numpy as np
class UniqueArray:

    """ 
    function to find if the given array has only unique elements. Iterative Approach
    """
    def is_unique(self, arr):
        temp_arr = []
        for i in range(len(arr)):
            if arr[i] in temp_arr:
                return False
            temp_arr.append(arr[i])
        return True
    
""" 
Create Object and calling the functions
"""
arr = np.array([1, 23, 45, 7, 8, 91, 23])
unique_array = UniqueArray()

result = unique_array.is_unique(arr)
print(result)