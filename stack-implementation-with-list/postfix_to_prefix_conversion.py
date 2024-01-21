"""
-------------------------------------------------------------------------------
Problem Statement: 
Postfix: An expression is called the postfix expression if the operator appears
in the expression after the operands. Simply of the form (operand1 operand2 operator). 

Example : AB+CD-* (Infix : (A+B) * (C-D) )

Prefix : An expression is called the prefix expression if the operator appears
in the expression before the operands. Simply of the form (operator operand1 operand2). 

Example : *+AB-CD (Infix : (A+B) * (C-D) )

Conversion of Postfix expression directly to Prefix without going through the 
process of converting them first to Infix
-------------------------------------------------------------------------------
"""

def is_operator(char):

    operators = { '+', '-', '*', '/'}
    return char in operators

def convert_to_prefix(expression):

    prefix_exp = []
    expression_length = len(expression)
    for i in range(expression_length):
        if is_operator(expression[i]):
            first_operand = prefix_exp[-1]
            prefix_exp.pop()
            second_operand = prefix_exp[-1]
            prefix_exp.pop()

            temp = expression[i] + first_operand + second_operand
            prefix_exp.append(temp)
        else:
            prefix_exp.append(expression[i])

    print(prefix_exp)

postfix_expression = "AB+CD-*"
convert_to_prefix(postfix_expression)


