""" 
Python program to demonstrate the deletion of the element from the python dictionary 
"""

class ElementDeletion:

    """ 
    Function show deletion of element --> pop() operation 
    """

    def pop_operation(self, my_dict, element):
        popped_element = my_dict.pop(element)
        return popped_element, my_dict
    
    """ 
    Funtion to remove an arbitary element from the python dictionary ( any random element)
    """
    def popitem_operation(self, my_dict):
        popped_item = my_dict.popitem()
        return popped_item, my_dict






""" 
Object Creation and function calls
"""
my_dict = {'Name': 'Neeraj', 'age': 26, 'job': 'Software Developer', }
element = 'Name'

delete_element = ElementDeletion()
# pop_result = delete_element.pop_operation(my_dict, element)
# print(pop_result)

popitem_result = delete_element.popitem_operation(my_dict)
print(popitem_result)