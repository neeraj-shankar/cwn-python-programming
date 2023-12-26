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


def funnyString(s):
    reversed_str = s[::-1]
    original_str_list = []
    reverse_str_list = []

    for i in range(1, len(s)):
        ascii_value_diff = abs(ord(s[i]) - ord(s[i-1]))
        original_str_list.append(ascii_value_diff)

        #Reversed String ascii value
        rev_ascii_value_diff = abs(ord(reversed_str[i]) - ord(reversed_str[i-1]))
        reverse_str_list.append(rev_ascii_value_diff)
    
    print(f"Original List: {original_str_list}")
    print(f"Revered List: {reverse_str_list}")
    if original_str_list == reverse_str_list:
        return "Funny"
    else:
        return "Not Funny"
    

def is_funny(s):

    reversed_string = s[::-1] # Create a copy of the string in reverse

    # Calculate the absolute differences in ASCII values for both strings
    diffs = [abs(ord(s[i]) - ord(s[i-1])) for i in range(1, len(s))]
    reversed_diff = [abs(ord(reversed_string[i])-ord(reversed_string[i-1])) for i in range(1, len(reversed_string))]

    # Compare the lists of absolute differences
    if diffs == reversed_diff:
        return "Funny"
    else:
        return "Not Funny"


if __name__ == '__main__':
    fptr = open('result.txt', 'w')

    q = int(input("Please enter number of queries: ").strip())

    for q_itr in range(q):
        s = input("Please enter a string: ")

        result = is_funny(s)

        fptr.write(result + '\n')

    fptr.close()
