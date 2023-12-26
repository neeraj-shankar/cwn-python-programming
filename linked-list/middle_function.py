""" 
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
"""

class MiddleFunction:

    """ 
    Function to remove first and last element of the given list and show other elements
    """
    def middle(self, my_list):
        middle_list = my_list[1:len(my_list)-1]
        return middle_list
    
""" 
Create object and function call
"""
my_list = [1, 2, 3, 4]
middle_function = MiddleFunction()

result = middle_function.middle(my_list)
print(result)

