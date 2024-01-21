##############################################################################
## The list methods make it very easy to use a list as a stack, where the last
## element added is the first element retrieved (“last-in, first-out”). 
## To add an item to the top of the stack, use append(). 
## To retrieve an item from the top of the stack, use pop()
##############################################################################

original_stack = ['first', 'second', 'third']

# read from right to left --> imagine stack: last element to be on top

# using append to add item on top of stack
original_stack.append('fourth')
print(f"Updated Stack: {original_stack}")

# using pop to remove the last element arrived --> rightmost element in list
original_stack.pop()
print(f"Updated Stack after Pop: {original_stack}")