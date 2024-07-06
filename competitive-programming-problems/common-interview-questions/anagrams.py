"""
Problem Statement:
-----------------------------------------------------------
An anagram is a word or phrase formed by rearranging the letters of another, 
such as "listen" and "silent". Find if two given strings are anagrams
-----------------------------------------------------------
"""


class AnagramWord:

    def __init__(self, input_data_first, input_data_second) -> None:

        self.input_data_first = input_data_first
        self.input_data_second = input_data_second

    def are_anagrams_sort(self):

        return sorted(self.input_data_first) == sorted(self.input_data_second)

    def are_anagrams_dict(self):
        """
        Check if two strings are anagrams using a dictionary.

        Anagrams are two strings that have the same characters but in a different order.

        Returns:
            bool: True if the two strings are anagrams, False otherwise.
        """

        # Check if the lengths of the two strings are different
        if len(self.input_data_first) != len(self.input_data_second):
            return False
        
        # Initialize dictionaries to store character frequencies of each string
        first_word_dict = {}
        second_word_dict = {}

        # Populate the first_word_dict with character frequencies from the first string
        for char in self.input_data_first:
            first_word_dict[char] = first_word_dict.get(char, 0) + 1

        # Populate the second_word_dict with character frequencies from the second string
        for char in self.input_data_second:
            second_word_dict[char] = second_word_dict.get(char, 0) + 1

        # Check if the two dictionaries are equal
        return first_word_dict == second_word_dict


if __name__ == "__main__":

    raw_data_first = "silent"
    raw_data_second = "listen"

    result = AnagramWord(raw_data_first, raw_data_second).are_anagrams_sort()
    print(f"Are the given words anagram?: {result}")

    result = AnagramWord(raw_data_first, raw_data_second).are_anagrams_dict()
    print(f"Are the given words anagram?: {result}")
