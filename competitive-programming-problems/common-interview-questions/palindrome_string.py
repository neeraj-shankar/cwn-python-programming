"""
Problem Statement: Verify if a given string is palindrome

Sample Example
----------------------------------------------------------
Input: "abcba"
Ouput: The given string is palindrome
----------------------------------------------------------
"""
from collections import deque

class PalindromeString:

    def __init__(self, input_data) -> None:
        self.input_data = input_data

    def first_approach(self):

        # Reverse the input string
        reversed_data = self.input_data[::-1]

        # Verify if the given string is palindrome
        if self.input_data == reversed_data:
            return True
        else:
            return False

    def is_palindrome_iterative(self):

        i, j = 0, len(self.input_data) - 1
        while i < j:
            if self.input_data[i] != self.input_data[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def is_palindrome_deque(self):

        chars = deque(self.input_data)
        print(chars)
        while len(chars) > 1:
            if chars.popleft() != chars.pop():
                return False
        
        return True


if __name__ == "__main__":

    raw_data = "abcba"

    result = PalindromeString(raw_data).first_approach()
    print(f"Is the Given String a Palindrome ?: {result}")

    result = PalindromeString(raw_data).is_palindrome_iterative()
    print(f"Is the Given String a Palindrome ?: {result}")

    result = PalindromeString(raw_data).is_palindrome_deque()
    print(f"Is the Given String a Palindrome ?: {result}")
