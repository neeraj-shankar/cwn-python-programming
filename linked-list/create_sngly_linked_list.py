"""
Basic Understanding of the Single Linked List
"""

# Create a node class to store Node value and next node address
class Node:
    def __init__(self, value=None):
        self.value = value # -----------------------------------------> O(1)
        self.next = None # -----------------------------------------> O(1)


# class for the single linked list 
class SingleLinkedLinked:

    
    """
    Initializing head and tail as null
    """
    def __init__(self):
        self.head = None # -----------------------------------------> O(1)
        self.tail = None # -----------------------------------------> O(1)


"""
Object Creation and value assigments
"""
singly_linked_list = SingleLinkedLinked()

# Node Class object and invoking the constructor
node1 = Node(1)
node2 = Node(2)

# Value assignment and address pointing
singly_linked_list.head = node1 # -----------------------------------------> O(1)
singly_linked_list.head.next  = node2 # -----------------------------------------> O(1)
singly_linked_list.tail = node2 # -----------------------------------------> O(1)


