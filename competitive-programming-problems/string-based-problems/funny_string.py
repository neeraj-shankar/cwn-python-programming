"""
In this challenge, you will determine whether a string is funny or not. To determine whether a string is funny, 
create a copy of the string in reverse e.g. abc-->bca . Iterating through each string, compare the absolute difference in the 
ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. If the list of absolute differences 
is the same for both strings, they are funny.

Determine whether a give string is funny. If it is, return Funny, otherwise return Not Funny.

"""

import math
import os
import random
import re
import sys


class FunnyStringCompilation:
    """A class to perform operations related to funny strings."""

    def __init__(self, input_string: str) -> None:
        """
        Initialize the FunnyStringCompilation object with the input string.

        Args:
            input_string (str): The input string to process.
        """

        self.input_string = input_string
        self.reversed_string = self.input_string[::1]

    def funny_string_loop(self):
        """
        Determine if the input string is funny using loop implementation.

        Returns:
            str: "Funny" if the string is funny, "Not Funny" otherwise.
        """

        abs_diff_original_str = []
        abs_diff_reversed_str = []

        for i in range(1, len(s)):
            ascii_value_diff = abs(
                ord(self.input_string[i]) - ord(self.input_string[i - 1])
            )
            abs_diff_original_str.append(ascii_value_diff)

            # Reversed String ascii value
            rev_ascii_value_diff = abs(
                ord(self.reversed_string[i]) - ord(self.reversed_string[i - 1])
            )
            abs_diff_reversed_str.append(rev_ascii_value_diff)

        if abs_diff_original_str == abs_diff_reversed_str:
            return "Funny"
        else:
            return "Not Funny"

    def funny_string_list_comprehension(self):
        """
        Determine if the input string is funny using list comprehension implementation.

        Returns:
            str: "Funny" if the string is funny, "Not Funny" otherwise.
        """

        reversed_string = s[::-1]

        # Calculate the absolute differences in ASCII values for both strings
        abs_diff_original_str = [
            abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s))
        ]
        abs_diff_original_str = [
            abs(ord(reversed_string[i]) - ord(reversed_string[i - 1]))
            for i in range(1, len(reversed_string))
        ]

        # Compare the lists of absolute differences
        if abs_diff_original_str == abs_diff_original_str:
            return "Funny"
        else:
            return "Not Funny"


if __name__ == "__main__":
    fptr = open("result.txt", "w")

    q = int(input("Please enter number of queries: ").strip())

    for q_itr in range(q):
        s = input("Please enter a string: ")

        result = FunnyStringCompilation(s).funny_string_list_comprehension()

        fptr.write(result + "\n")

    fptr.close()
