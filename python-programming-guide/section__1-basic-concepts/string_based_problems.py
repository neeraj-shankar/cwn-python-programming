"""
Reverse a String:

Question: Write a function to reverse a string.
Tests: Understanding of string slicing, iteration, and basic string manipulation.
Check for Palindrome:

Question: Write a function to check if a given string is a palindrome.
Tests: Knowledge of string indexing and comparison.
Anagram Check:

Question: Write a function to determine if two strings are anagrams.
Tests: Understanding of sorting, dictionaries, or counter collections.
Count the Occurrences of Each Character:

Question: Write a function to count the occurrences of each character in a string.
Tests: Ability to use dictionaries and string iteration.
First Non-Repeating Character:

Question: Write a function to find the first non-repeating character in a string.
Tests: String traversal and usage of dictionaries for counting characters.
Longest Common Prefix:

Question: Write a function to find the longest common prefix string amongst an array of strings.
Tests: Ability to handle multiple strings, string comparison.
Substring Search:

Question: Implement a function to find all occurrences of a substring in a given string.
Tests: Understanding of substring search methods (find, index), loops.
String Compression:

Question: Write a function to perform basic string compression using the counts of repeated characters (e.g., "aabcccccaaa" becomes "a2b1c5a3").
Tests: String manipulation, understanding of run-length encoding.
Valid Parentheses:

Question: Write a function to determine if a string containing parentheses is valid. A string is considered valid if parentheses are closed in the correct order.
Tests: Stack usage, string traversal.
Remove Duplicates:

Question: Write a function to remove duplicate characters from a string.
Tests: String traversal, use of sets or dictionaries to track seen characters.

"""
import re

class StringPracticeSet:

    def __init__(self) -> None:
        pass

    @staticmethod
    def reverse_string():
        """
        Takes a python string as input, reverse the sequence of characters and prints on console
        """
        input_string = "iamneerajshankar"
        reversed_string_using_negative_indexing = input_string[
            -1::-1
        ]  # raknahsjareenmai
        reversed_string_slicing = input_string[::-1]  # raknahsjareenmai

        print(
            f"Reversed String using negative indexing: {reversed_string_using_negative_indexing}"
        )
        print(f"Reversed String using Slicing: {reversed_string_slicing}")

    @staticmethod
    def check_palindrome():
        """
        A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces,
        punctuation, and capitalization). In other words, if you reverse the sequence, it remains unchanged.

        Takes list of strings and returns a list of Boolean (True for Palindrome and False for Non-Palindrome)

        """
        original_string_list = [
            "radar",
            "level",
            "civic",
            "name",
            "madam",
            "last",
            "rotor",
            "A man, a plan, a canal, Panama",
            "Was it a car or a cat I saw?",
        ]

        is_palindrome_list = []
        for word in original_string_list:
            # Remove non-alphanumeric characters and convert to lower case
            cleaned_word_phrase= re.sub(r'[^A-Za-z0-9]', '', word).lower()  
            print(cleaned_word_phrase)        
            if cleaned_word_phrase == cleaned_word_phrase[::-1]:
                is_palindrome_list.append("YES")
            else:
                is_palindrome_list.append("NO")

        print(f"Palindromes: {is_palindrome_list}")


if __name__ == "__main__":

    # Creating instance of the StringPracticeSet
    stringPracticeSet = StringPracticeSet()

    # Testing reverse_string() method
    stringPracticeSet.reverse_string()

    # Testing check_palindrome() method
    stringPracticeSet.check_palindrome()
