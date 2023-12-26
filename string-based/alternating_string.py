"""
-----------------------------------------------------------------------------------------------------------------------

Problem Statement:
You are given a string containing characters A and B only. Your task is to change it into a string such that there are no 
matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

Objective:
Your task is to find the minimum number of required deletions.

Example Input:
raw_data = "AAABBB"

Example Output:
Number of Deletion Required: 4

"""


def alternate_string(input_string):
    number_of_deletion = 0
    final_string = []
    base_char = input_string[0]  # This will be used for comparison
    final_string.append(base_char)
    for char in input_string[1:]:
        # if the current character is same as the base char, its duplicate (matching adjacent character)
        # Need to be removed, deletion count increases
        if base_char == char:
            number_of_deletion += 1
        else:
            # otheriwse, base character to be updated with current character
            base_char = char
            final_string.append(char)
    print(f"Final String: {final_string}")
    return number_of_deletion


if __name__ == "__main__":
    raw_data = "AAABBB"
    result = alternate_string(raw_data)
    print(f"Number of Deletion Required: {result}")  # Number of Deletion Required: 4
