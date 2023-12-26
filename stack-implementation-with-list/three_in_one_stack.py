"""
given a list of size n, create 3 different stack of equal size
"""


class MultiStack(object):

    # constructor to initialize attributes of list and stack to be constructed
    def __init__(self, stack_size):
        self.number_of_stack = 3
        self.custom_list = [0] * (stack_size * self.number_of_stack)
        self.sizes = [0] * self.number_of_stack
        self.stack_size = stack_size

    # Check if the stack is empty
    # returns true in case stack is empty else returns false
    def is_empty(self, stack_number):
        if self.stack_size[stack_number] == 0:
            return True
        else:
            return False

    # Check if the stack is full
    # returns true in case stack is empty else returns false
    def is_full(self, stack_number):
        if self.stack_size[stack_number] == self.stack_size:
            return True
        else:
            return False


    

