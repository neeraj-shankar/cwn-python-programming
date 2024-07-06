""" 
Selection sort works in a way that at completion of one iteration, the smallest element is moved to the sorted part of the array

Time complexity --> O(n^2)
Space complexity --> O(1)

when to use
---------------------------
1. when space is insufficient
2. easy to emplement

when not to use
----------------------------
1. Time is a concern
"""


def selection_sort(custom_list):
    for i in range(len(custom_list)):
        # index of the smallest element
        min_index = i
        for j in range(i + 1, len(custom_list)):
            # update min index if smaller element found
            if custom_list[min_index] > custom_list[j]:
                min_index = j

            # finally swap the element - move smallest element to sorted side
        custom_list[i], custom_list[min_index] = custom_list[min_index], custom_list[i]
    return custom_list


year_list = [2013, 1994, 2000, 2001, 1999, 2000, 1876, 1900]
sorted_year_list = selection_sort(year_list)
print(f"The sorted list of years using selection sort --> {sorted_year_list}")
