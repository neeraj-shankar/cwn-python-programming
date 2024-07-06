"""
-----------------------------------------------------------------------------------------------------------------------

Problem Statement:
You are given a string containing characters A and B only. Your task is to change it into a string such that there are
no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

Objective:
Your task is to find the minimum number of required deletions.

Example Input:
raw_data = "AAABBB"

Example Output:
Output: "AB"
Number of Deletion Required: 4

-----------------------------------------------------------------------------------------------------------------------
"""


class AlternateStringProblem:

    def first_approach(input_string):
        number_of_deletion = 0
        final_string = [] # Not required for finding solution
        key = input_string[0]  # This will be used for comparison
        final_string.append(key) 
        for char in input_string[1:]:
            # if the current character is same as the base char, its duplicate (matching adjacent character)
            # Need to be removed, deletion count increases
            if key == char:
                number_of_deletion += 1
            else:
                # otherwise, base character to be updated with current character
                key = char
                final_string.append(char) 
        print(f"Final String: {final_string}")
        return number_of_deletion
    
    def second_approach(raw_data):

        # count the occurence each character in string
        char_count = {}

        for chr in raw_data:
            char_count[chr] = char_count.get(chr, 0) + 1
            print(f"The dict status: {char_count}")
        
        # Find the maximum count of any character
        max_count = max(char_count.values(), default=0)

        # Calculate the number of deletion required
        return len(raw_data) - max_count


if __name__ == "__main__":
    raw_data = "AAABBB"
    raw_data = "aabbbccdd"


    first_result = AlternateStringProblem.first_approach(raw_data)
    print(f"Number of Deletion Required: {first_result}")  # Number of Deletion Required: 4

    second_result = AlternateStringProblem.second_approach(raw_data)
    print(f"Number Deletion required: {second_result}")
