"""
-----------------------------------------------------------------------------------------------------------------------
Amanda has a string of lowercase letters that she wants to copy to a new string. She can perform the following operations
with the given costs. She can perform them any number of times to construct a new string p:

1. Append a character to the end of string p at a cost of 1 dollar.
2. Choose any substring of p and append it to the end of  at no charge.

Example
-----------------------------------------------------------------------------------------------------------------------
1. String --> abcd, total cost --> 4
2. String --> abab, total cost --> 2
"""

class StringConstruction:

    def __init__(self, s):
        self.input_string = s

    def using_naive_approach(self):
        total_cost = 0
        new_string = ''

        for char in self.input_string:
            if char in new_string:
                new_string = new_string + char
            else:
                new_string = new_string + char
                total_cost += 1

        print(new_string)
        print(f"Total Cost: {total_cost}")
        return total_cost

if __name__ == "__main__":

    original_string = "abab"
    StringConstruction(original_string).using_naive_approach()