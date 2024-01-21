##############################################################################
## Implementation of stack in python using list with defined size
##############################################################################


class Stack:
    def __init__(self, maxSize):
        """
        Initialize an empty list and sets a varibale to define max size of it.
        """
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        """
        Reverse the list in constructor and return it in form of string.
        """
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    # isEmpty
    def isEmpty(self):
        """
        Verify if the stack is empty and returns binary result of it.
        :params None
        :returns True: if stack is empty else False
        """
        if self.list == []:
            return True
        else:
            return False

    # isFull
    def isFull(self):
        """
        Verify if the stack is full and returns binary result of it.
        :params None
        :returns True: if stack reached max size else False
        """
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    #  Push
    def push(self, value):
        """
        Accepts User Value and insert it at top of the stack
        :params Value--> Element to be put on top of stack
        :returns Message whether the element can be inserted or not in the stack
        """
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"

    # Pop
    def pop(self):
        """
        Removes the top element in the stack and returns the element remvoed.
        :params None
        :returns Top Element of the of the stack that is removed.
        """
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

    # peek
    def peek(self):
        """
        Shows the elements on the top of stack
        :params None
        :return Message if no element in stack else the element found.
        :Disclaimer It does not remove element from the stack
        """
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list) - 1]

    #  delete
    def delete(self):
        self.list = None


customStack = Stack(4)

# Checking if stack is empty or full before making any operation
print(
    f"Result of {customStack.isEmpty.__name__} before pushing any element: {customStack.isEmpty()}"
)
# Result of before pushing any element: isEmpty: True
print(
    f"Result of {customStack.isFull.__name__} before pushing any element: {customStack.isFull()}"
)
# Result of before pushing any element: isFull: False

# Adding some element to the stack
customStack.push(1)
customStack.push(2)
customStack.push(3)

# Showing stack after adding some element
print(f"Result after adding some element: {customStack}")

# We declared stack size to be 4. Lets check it after adding 4th element
customStack.push(4)
print(f"Result of after pushing maximum elements: isEmpty: {customStack.isEmpty()}")
# Result of after pushing maximum elements: isEmpty: False
print(f"Result of before pushing maximum elements: isFull: {customStack.isFull()}")
# Result of before pushing maximum elements: isFull: True

# Showing stack after popping one element from it
res = customStack.pop()
print(f"The element removed from top of stack: {res}")
print(f"Current state of stack after pop operation: {customStack}")
