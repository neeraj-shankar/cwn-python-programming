""" 
Handling missing key value error in pytho dictionary 
"""


class MissingKeys:

    """ 
    using the get() method to fetch the value
    """
    @staticmethod
    def using_get_method(custom_dictionary):
        print(f"{custom_dictionary.get('name', 'The key not found')}")
        print(f"{custom_dictionary.get('Neeraj', 'The key not found')}")

    """ 
    using setdefault() method
    """
    @staticmethod
    def using_set_default(custom_dictionary):
        custom_dictionary.setdefault("Japan", "The key does not exist")
        print(f'{custom_dictionary["Japan"]}')
        print(f'{custom_dictionary["Neeraj"]}')
        

""" 
Calling class methods
"""

name_and_roll = {"Neeraj": 1, "Ankit": 4, "Anchal": 3, "John": 2}
MissingKeys.using_get_method(name_and_roll)
MissingKeys.using_set_default(name_and_roll)
