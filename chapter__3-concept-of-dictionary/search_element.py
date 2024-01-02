""" 
Python program to demonstrate the element search within a dictionary
"""

class ElementSearch:

    """ 
    Naive Approach
    # Time Complexity --> O(n) and Space Complexity --> O(1)
    """
    def search_element(self, my_dict, value):

        for key in my_dict: # -----------------------------> O(n)
            if my_dict[key] == value: # -----------------------------> O(1)
                return f"The element found for key--> {key}" # -----------------------------> O(1)
        
        return f"The element does not exist" # -----------------------------> O(1)
    

""" 
Object creation and function calls
"""

my_dict = {'Name': 'Neeraj', 'age': 26, 'job': 'Software Developer', }
value = 'Neeraj'
element_search = ElementSearch()
result = element_search.search_element(my_dict, value)
print(result)