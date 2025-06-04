"""
A python program to understand the different use case map()
"""
from format_output import use_case_separator

#####################################################################################################################
# Adding the list form one by adding respective index elements
#####################################################################################################################
odd_numbers = [1, 3, 5, 7]
even_numbers = [2, 4, 6, 8]

new_numbers = list(map(lambda x, y: x + y, odd_numbers, even_numbers))
use_case_separator()
print(f"The new numbers list as --> {new_numbers}")


#####################################################################################################################
# Stringify the list strings into list of characters of the string items in list
#####################################################################################################################
# Time complexity: O(n), where n is the number of elements in the input list l.
# Auxiliary space: O(n), as the resulting list test contains n sub lists, each of which contains a single character.
string_list = ['cat', 'dog', 'tiger']
characters_list = list(map(list, string_list))
use_case_separator()
print(f"The original string list --> {string_list}")
print(f"the output characters list --> {characters_list}")


#####################################################################################################################
# Define a function to double the even number and leave odd numbers
#####################################################################################################################

def double_even_number(any_num):
    if any_num % 2 == 0:
        return any_num * 2
    else:
        return any_num


numbers_list = [1, 2, 3, 4, 5, 6, 7]
doubled_number_list = list(map(double_even_number, numbers_list))
use_case_separator()
print(f"The original list of numbers --> {numbers_list}")
print(f"The new list with even numbers doubled --> {doubled_number_list}")
