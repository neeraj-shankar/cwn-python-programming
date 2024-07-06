"""
Problem statement: examine whether the pairs and the orders of “{“, “}”, 
“(“, “)”, “[“, “]” are correct in the given expression.

Solution: The idea is to put all the opening brackets in the stack. Whenever
you hit a closing bracket, search if the top of the stack is the opening 
bracket of the same nature. If this holds then pop the stack and continue the 
iteration. In the end if the stack is empty, it means all brackets are balanced
or well-formed. Otherwise, they are not balanced

Example Positive: 
Output: 

Example Negative:
Output: 

Time complexity:
O(n): The time complexity is O(n), where n is the length of the input 
expression. In the worst case, you need to iterate through each character
in the expression once

Space Complexity: 
O(n), where n is the length of the input expression. In the worst case, when
all opening brackets are encountered and pushed onto the stack, the stack can
have at most n/2 elements. This occurs when the expression is composed entirely
of opening brackets.
"""


def is_balanced(expression):
    stack = []

    # hold the pair of opening and corresponding brackets
    brackets = {"(": ")", "[": "]", "{": "}"}

    for char in expression:
        if char in brackets.keys():  # Opening bracket
            stack.append(char)
        elif char in brackets.values():  # Closing bracket
            if not stack or brackets[stack.pop()] != char:
                print("I am if of elif")
                return False

    # Check if there are any remaining unmatched opening brackets
    return not stack


# Test cases
print(is_balanced("(){}[]"))  # Output: True
print(is_balanced("{[()]}"))  # Output: True
print(is_balanced("({[()]})"))  # Output: True
print(is_balanced("({[()])}"))  # Output: False
print(is_balanced("({[()]"))  # Output: False
