"""
Python program to identify the balanced brackets in the given list of bracket
"""
from format_output import use_case_separator


class BalancedBracketsValidation:

    open_bracket_list = ["{", "[", "("]
    close_bracket_list = ["}", "]", ")"]

    """
    Verify the existence balanced brackets using the stack
    """
    def using_stack_option(self, input_string):

        # if open bracket is encountered put it in the stack
        # if close bracket is found in input data pop out from stack
        # check if the stack is empty
        bracket_stack = []
        for i in input_string:
            if i in self.open_bracket_list:
                bracket_stack.append(i)
            elif i in self.close_bracket_list:
                pos = self.close_bracket_list.index(i)
                print(f"The index position of the closed bracket list --> {pos}")
                if len(bracket_stack)> 0 and self.open_bracket_list[pos] == bracket_stack[len(bracket_stack)-1]:
                    bracket_stack.pop()
                else:
                    return "unbalanced"

        if len(bracket_stack) == 0:
            print(f"The parenthesis are balanced")
            assert True, "The parenthesis are balanced"

        else:
            assert False, "The parenthesis not balanced"


"""
input data, object creation and function calls
"""

bracket_string = "(()(()))"

test_obj = BalancedBracketsValidation()

use_case_separator()
test_obj.using_stack_option(bracket_string)
