"""
Demonstratio of the inserting data (Node) in a linked list in different ways
1. Create a node class for the linked list node. [ Node class--> Data Field and Address Field for next node]
2. Create Linked List class and initialize Linked List object using constructor
3. print_list to traverse through linked list and show all data 
"""

# Node Class
class Node:
    # function to initialize node object
    def __init__(self, value=None):
        self.value = value # -------------------------------------------------> O(1)
        self.next = None # -------------------------------------------------> O(1)


# Linked Linked Class

class LinkedList:
    
    # function to initialize the LinkedList object
    def __init__(self):
        self.head = None # -------------------------------------------------> O(1)
        self.tail = None # -------------------------------------------------> O(1)
    

    # function to print the linked list data
    def print_list(self):
        temp = self.head # -------------------------------------------------> O(1)
        print(f"The stored in the provided linked list is as follows: ", end=" ")
        while (temp): # -------------------------------------------------> O(n)
            print(temp.value, end=" ") 
            temp = temp.next # -------------------------------------------------> O(1)
        print("\n")


    # function to insert data at the beginning of the linked list
    def push(self, new_value):

        # allocate new value to a temp node --> new_node
        new_node = Node(new_value) # -------------------------------------------------> O(1)

        # given next of new_node to the head
        new_node.next = self.head # -------------------------------------------------> O(1)

        # point the head to the new_node
        self.head = new_node # -------------------------------------------------> O(1)
    
    # function to insert the the given position in the linked list 
    def insert_after(self, prev_node, new_value):

        # 1. Creating an new node and initializing with new value
        new_node = Node(new_value)

        # 2. Making the next of the prev node as the next of the new node
        new_node.next = prev_node.next

        # 3. Making the previous node as new node
        prev_node.next = new_node
    
    # function add node at the end of the linked list
    def append(self, new_value):
        # 1. create new node and initialize the new value
        new_node = Node(new_value)

        # 2. Check if the Linked List is empty and if so, assign make new node as head
        if self.head == None:
            self.head = new_node
            return

        # 3. Traverse through entire linked list until reached last node
        temp = self.head
        while(temp.next):
            temp = temp.next 
        temp.next = new_node
"""
Object creation, Value assignment and function calls
"""

linked_list = LinkedList()

# calling the push method to insert node at begining of the list 
linked_list.push(2)
linked_list.push(3)
linked_list.push(4)

# Call for append method to insert new node at the end
linked_list.append(5)


# calling the insert at method to insert a new node after a specified node
linked_list.insert_after(linked_list.head, 7)

# calling the print method to display linked list data
linked_list.print_list()

