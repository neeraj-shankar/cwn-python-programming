"""

Questions Covered in this file
---------------------------------------------------------------------------------------------------
1. How would you merge two dictionaries in Python? Provide an example.

2. Given a dictionary, how can you reverse the mapping, turning values into keys and keys into values?

3. Write a Python function that takes a list of tuples and converts it into a dictionary, where the first element of each tuple becomes the key and the second element becomes the value.

4. How can you create a dictionary that maintains the order of items as they are added?

5. Explain the difference between the `get` and `[]` methods when retrieving the value associated with a key in a dictionary.

6. How would you check if a dictionary contains a specific key and, if it does, increment its value?

7. Write a Python program to remove duplicates (based on values) from a dictionary.

8. How can you combine the values of two dictionaries into a list, where each list item is a tuple consisting of the key and the two corresponding values from each dictionary?

9. Given a dictionary, how would you find the key with the maximum value?

10. Write a Python function that takes a dictionary and returns a list of keys sorted by their corresponding values.
---------------------------------------------------------------------------------------------------

"""
from collections import defaultdict

class DictionaryPracticeSet:

    def __init__(self) -> None:
        pass

    @staticmethod
    def merge_dictionaries():
        """
        Merges two dictionaries into one and prints result on console.
        """

        first_dictionary = {
            "name": "Alex",
            "place": "Washington",
            "age": 29,
            "is_graduated": False,
        }

        second_dictionary = {"country": "USA", "is_married": True}

        # Using merge operator. Time Complexity: O(n + m), Space Complexity: O(n + m)
        merged_dictionary = first_dictionary | second_dictionary
        print(f"Merged Dictionary using Merge Operator: {merged_dictionary}")
        
        # Using Update method, Time Complexity: O(n), Space Complexity: O(1)
        first_dictionary.update(second_dictionary)
        print(f"The Merged Version of two dict: {first_dictionary}")

    @staticmethod
    def reverse_mapping():
        """
        Reverses the mapping of the dictionary. Key becomes value and Value becomes Key.
        """

        first_dictionary = {
            "name": "Alex",
            "place": "Washington",
            "age": 29,
            "is_graduated": False,
        }

        # for key, value in first_dictionary.items():
        #     value[key] = key

        # Using the dictionary comprehension
        reversed_dictionary = {value: key for key, value in first_dictionary.items()}

        print(reversed_dictionary)


    @staticmethod
    def reverse_mapping_preserve_non_unque_values():
        """
        Reverses the mapping of the dictionary. Key becomes value and Value becomes Key.
        reverse the dictionary to a structure where each new key maps to a list of original keys
        """
        original_dictionary = {'a': 1, "b": 1, "c": 2, "d": 3}

        reversed_dictionary = defaultdict(list)
        print(f"Initialized Reversed Dict: {reversed_dictionary}")

        for key, value in original_dictionary.items():
            reversed_dictionary[value].append(key)
        
        print(f"Reversed Version of the dictionary: {reversed_dictionary}")

    @staticmethod
    def convert_tuple_into_dict():
        """
        Takes a list of tuples and converts it into a dictionary, where the first element of each tuple becomes the key and the second element becomes the value.
        """
        name_and_city = [("Neeraj", "Pune"), ("Ankit Sihna", "Patna", "Indore"), ("Ankit Asati", "Indore")]
        print(name_and_city)
        data_dict = {}

        for detail in name_and_city:
            data_dict[detail[0]] = detail[1:]
        print(data_dict)

    @staticmethod
    def increment_the_key():
        """
        Check if a dictionary contains a specific key and, if it does, increment its value?
        """

        number_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}

        desired_key = "a"
        
        if desired_key in number_dictionary:
            number_dictionary[desired_key] += 1
        print(f"Resultant after key-increment: {number_dictionary}")

    @staticmethod
    def remove_duplicates():

        number_dictionary = {"a": 1, "b": 2, "c": 2, "d": 4}
        pass




if __name__ == "__main__":

    # DictionaryPracticeSet().merge_dictionaries()
    # DictionaryPracticeSet().reverse_mapping()
    # DictionaryPracticeSet().reverse_mapping_preserve_non_unque_values()
    # DictionaryPracticeSet().convert_tuple_into_dict()
    DictionaryPracticeSet().increment_the_key()