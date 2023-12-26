"""
There is a sequence of words in CamelCase as a string of letters, s, having the following properties:

1. It is a concatenation of one or more words consisting of English letters.
2. All letters in the first word are lowercase.
3. For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

Given s, determine the number of words in s.
"""
import re


class CamelCaseWordCount:

    """
    Using the regex to solve the problem
    """

    @staticmethod
    def using_regex(input_string):
        expression = r"[A-Z][a-z]*"
        words_with_capital_letters = len(re.findall(expression, input_string)) + 1
        print(f"The total count of words -->{words_with_capital_letters}")

    """
    using the looping technique to find the same
    """

    @staticmethod
    def using_loop_is_upper(input_string):
        # Initialize all the word count to 1 for first small letter word
        word_count = 1
        for char in input_string:
            if char.isupper():
                word_count += 1
        print(f"The total word count using loop and isupper()--> {word_count}")


"""
Input data, function calls, etc
"""
in_str = "camelCaseStringExample"

CamelCaseWordCount.using_regex(in_str)
CamelCaseWordCount.using_regex(in_str)
