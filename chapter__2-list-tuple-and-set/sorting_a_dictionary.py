""" 
Programs to short a given python dictionary in various ways
"""
import numpy as np


class DictionarySort:

    @staticmethod
    def just_for_formatting():
        print("=======================================================================================================")

    """ 
    By sorting the key
    """
    @staticmethod
    def sort_by_key(custom_dictionary):

        sorted_keys = list(custom_dictionary.keys())
        sorted_keys.sort()
        print(f"The sorted keys in list form--> {sorted_keys}")

        # using list comprehension to form new dictionary using the sorted keys
        sorted_ranking = {i: custom_dictionary[i] for i in sorted_keys}
        print(f"The ranking list of the languages --> {sorted_ranking}")

    """ 
    Using the sorted method to sort keys in dictionary and then print them
    """
    @staticmethod
    def display_sorted_keys(custom_dictionary):

        print(f"The original order of the keys -->", end=" ")
        for key in custom_dictionary:
            print(key, end=" ")
        print("\n")

        # using the sorted method
        print(f"The keys in sorted order -->", end=" ")
        for key in sorted(custom_dictionary.keys()):
            print(key, end=" ")
        print("\n")

    """ 
    Using the OrderDict class from collection to sort the dictionary by keys
    """
    @staticmethod
    def sort_by_collection_module(custom_dictionary):
        sorted_ranking = sorted(custom_dictionary.items())
        print(f"I don't know --> {sorted_ranking}")

    @staticmethod
    def sort_by_value(custom_dictionary):

        # Separate the keys and values in a list form
        my_keys = list(custom_dictionary.keys())
        values = list(custom_dictionary.values())
        sorted_values_index = np.argsort(values)
        print(f"The sorted index of values in dictionary --> {sorted_values_index}")

        # combine the values and keys in order to form ordered dictionary
        ordered_ranking = {my_keys[i]: values[i] for i in sorted_values_index}
        print(f"The sorted dictionary based on values --> {ordered_ranking}")


""" 
Calling the different sorting techniques
"""

language_ranking = {3: "Java", 1: "Python", 2: "Javascript", 5: "cplusplus", 4: "kotlin"}

name_and_roll = {"Neeraj": 1, "Ankit": 4, "Anchal": 3, "John": 2}

DictionarySort.sort_by_key(language_ranking)
DictionarySort.just_for_formatting()
DictionarySort.display_sorted_keys(language_ranking)
DictionarySort.just_for_formatting()
DictionarySort.sort_by_collection_module(name_and_roll)
DictionarySort.just_for_formatting()
DictionarySort.sort_by_value(name_and_roll)
