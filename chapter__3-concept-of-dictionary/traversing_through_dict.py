""" 
Python program to demonstrate the traversal of a dictionary.
"""


class DictionaryTraversal:

    """ 
    Naive Approach
    """
    def traverse_a_dict(self, my_dict):
        for key in my_dict: # -------------------------------->0(n)
            print(f'For Key --> {key}, the value is --> {my_dict[key]}') # -------------------------------->0(1)



""" 
Object and function calls
"""

my_dict = {'Name': 'Neeraj', 'age': 26, 'job': 'Software Developer', }
traversing = DictionaryTraversal()

traversing.traverse_a_dict(my_dict)