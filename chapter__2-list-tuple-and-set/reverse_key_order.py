""" 
Sometimes, while working with dictionary, we can have a problem in which we need to reverse the order of dictionary. 
This is quite a common problem and can have application in many domains including day-day programming
"""
from format_output import use_case_separator
from collections import deque, OrderedDict

class ReverseKeyOrder(object):
    # input dictionary for inversion
    animal_order = {"Tiger": 1, "Lion": 2, "Zebra": 3}

    """ 
    Method : Using loop + recursion
    """

    def using_loop_and_recursion(self):

        # Returns list of key-value wrapped as tuple of a given dictionary
        dict_into_list_of_tuple = list(self.animal_order.items())
        print(f"The list of keys --> {dict_into_list_of_tuple}")
        # dict_into_list_of_tuple.reverse()

        # reversed method to return the list reverses iterator object
        reversed_iterator = reversed(dict_into_list_of_tuple)
        print(f"The reversed list of tuples --> {reversed_iterator}")

        dict_with_revered_keys = dict(reversed_iterator)
        print(f"The dictionary with key reversed --> {dict_with_revered_keys}")

    def using_the_deque(self):
        print(f"The original dictionary --> {self.animal_order}")
        # we use the deque data structure from the collections module to reverse the order of the dictionary keys.
        # create a new dictionary object using a dictionary comprehension
        # reversed keys and original values and then
        # use dict() constructor to convert the new dictionary to an OrderedDict object.
        deque_the_keys = deque(self.animal_order.keys())
        print(f"The deque keys of the animal order dict --> {deque_the_keys}")
        print(f"The type of deque keys of the animal order dict --> {type(deque_the_keys)}")
        # calling the reverse() on deque keys to reverse the keys
        deque_the_keys.reverse()
        print(f"The reversed deque keys --> {deque_the_keys}")

        revered_key_dictionary = {key: self.animal_order[key] for key in deque_the_keys}
        print(f"The revered key in the dictionary --> {revered_key_dictionary}")


""" 
Object creation and function calls
"""
test_obj = ReverseKeyOrder()

use_case_separator()
test_obj.using_loop_and_recursion()

use_case_separator()
test_obj.using_the_deque()

