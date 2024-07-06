""" 
Python program to reverse a linked list using different approach 
"""

class Node:

    # Initialize the data and address field of the linked list
    def __init__(self, value=None):
        self.value = value # ----------------------------------> O(1)
        self.next = None # ----------------------------------> O(1)

class ReverseLinkedList:

    """ 
    Contructor to initialize the head node
    """
    def __init__(self) -> None:
        self.head = None # ----------------------------------> O(1)

    
    def format_console(self):
        print(f"===============================================================================================")

    """ 
    function to display the data available in each node of the linked list
    """
    def print_list(self):
        temp = self.head # ----------------------------------> O(1)
        print(f"The following data are stored in the linked list: ", end=" ") # ----------------------------------> O(1)
        while(temp):
            print(temp.value, end=" ") # ----------------------------------> O(1)
            temp = temp.next # ----------------------------------> O(1)
        print("\n")

    """ 
    function to insert the new node at the begining of the linked list 
    """
    def push(self, new_value):

        # creating a new node with new data
        new_node = Node(new_value) # ----------------------------------> O(1)

        # Making next of new node to point head node
        new_node.next = self.head # ----------------------------------> O(1)

        # Making the new node as head node
        self.head = new_node # ----------------------------------> O(1)
        

    """ 
    function to reverse a linked list by iterative approach 
    """
    def reverse_iterative(self): # Time complexity --. O(n), Space Complexity --> O(1) -- No additional space required 
        prev_node = None # ----------------------------------> O(1)
        current_node = self.head # ----------------------------------> O(1)
        next_node = None # ----------------------------------> O(1)

        while( current_node != None): # ----------------------------------> O(n)
            next_node = current_node.next # ----------------------------------> O(1)
            self.format_console()
            print(f"The next node address --> {next_node}")
            current_node.next = prev_node # ----------------------------------> O(1)
            self.format_console()
            print(f"Current Node Address in Memory --> {current_node}")
            print(f"Current Node Address Field Data in Memory --> {current_node.next}")
            self.format_console()
            prev_node = current_node # ----------------------------------> O(1)
            print(f"The previous node address in memory --> {prev_node}")
            current_node = next_node # ----------------------------------> O(1)
            print(f"The current node address in memory --> {current_node}")

        self.head = prev_node # ----------------------------------> O(1)



""" 
Object creation and function calls
"""
linked_list = ReverseLinkedList()

for i in range(1,5):
    linked_list.push(i)

linked_list.print_list()
linked_list.reverse_iterative()
linked_list.print_list()