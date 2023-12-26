""" 
Python program to demonstrate the various operations that can be performed using the stack
"""


class StackOperation:

    # constructor method to initialize the list
    def __init__(self):
        self.stacked_list = []  # ---------------------------------------> O(1)

    # Uses the stack_list initialized by the constructor
    # Reverses the stack_list and returns each element on top of each
    # This is done to achieve the demonstration of LIFO
    def __str__(self):
        values = self.stacked_list.reverse()
        values = [str(x) for x in self.stacked_list]
        return "\n".join(values)

    # Checks whether the given stack is empty and return True or False based on outcome
    def is_empty(self):
        if self.stacked_list == []:  # ---------------------------------------> O(1)
            return True
        else:
            return False

    # Takes the input data and insert it on the top of the stack
    def push(self, data):
        self.stacked_list.append(data)  # ---------------------------------------> O(1)
        return f"The element {data} pushed to the stack successfully"

    # Checks if given stack is empty.
    # If stack is not empty removes the top element of the stack
    def pop(self):
        if self.is_empty():
            return f"There is no element in the stack. "
        else:
            return self.stacked_list.pop()  # ---------------------------------------> O(1)/0(1)

    # Checks if the stack is empty
    # if not empty find and return the top element of the stack
    # It does not remove element from the stack
    def peek(self):
        if self.is_empty():
            return f"There is no element in the stack. "
        else:
            return self.stacked_list[len(self.stacked_list) - 1]


""" 
Creating StackOperation object, function calls, etc
"""
stack_operation = StackOperation()

# Pushing some elements to stack 
stack_operation.push(1)
stack_operation.push(2)
stack_operation.push(3)
stack_operation.push(4)
print(f"The elements in the stack: \n{stack_operation}")
stack_operation.pop()
print(f"The elements in the stack after pop:\n{stack_operation}")
print(f"Value extracted by the peek method: {stack_operation.peek()}")
print(f"The elements in the stack after peek: \n {stack_operation}")
