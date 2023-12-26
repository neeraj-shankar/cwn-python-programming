"""
Problem Statement
-----------------------------------------------------------------------------------------------------------------------
Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. In each operation,
select a pair of adjacent letters that match, and delete them.

Delete as many characters as possible using this method and return the resulting string. If the final string is empty,
return Empty String


"""


def super_reduced_string(s):

    char_stack = []

    for char in s:
        # checks if char_stack is not empty and top value matches char in s
        # once matched pop that character
        if char_stack and char_stack[-1] == char:
            char_stack.pop()
        # else adds the char to the stack
        else:
            char_stack.append(char)

    # fetch each char char_stack and join them as single string
    reduced_string = ''.join(char_stack)

    # returns reduced_string if reduced_string is not empty else returns ""
    return reduced_string if reduced_string else "Empty String"


"""
input data and function call
"""
fptr = open('output_file.txt', 'w')

input_string = input()

result = super_reduced_string(input_string)

fptr.write(result + '\n')

fptr.close()
