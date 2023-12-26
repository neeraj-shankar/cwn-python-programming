"""
Bubble Sort --> It is an algorthim where each time adjacent elements are compared and swapped as per increasing or decreasing order
and the process is repeated until the entire list is sorted 

Time Complexity --> O(n^2)
Space Complexity --> O(1)  

When to user bubble sort
--------------------------
1. when the given input is already sorted 
2. space is a concern
3. easy to implement

when to not use 
--------------------------
1. Where time complexity matters

"""


class BubbleSortAlgorithm:


    """ 
    Applying the bubble sort on regular list 
    """
    @staticmethod
    def sort_list_non_decreasing_order(custom_list):

        total_items = len(custom_list)

        for i in range(total_items-1):
            for j in range(total_items-i-1): # every time largest element reach correct its right place (-i)
                if custom_list[j] > custom_list [j+1]:
                    custom_list[j], custom_list[j+1] = custom_list[j+1], custom_list[j]

        return custom_list


""" 
Calling the different sorting methods technique
"""

year_list = [2013, 1994, 2000, 2001, 1999, 2000, 1876, 1900]

sorted_list = BubbleSortAlgorithm.sort_list_non_decreasing_order(year_list)
print(f"The given list of years --> {year_list}")
print(f"The sorted year list --> {sorted_list}")
