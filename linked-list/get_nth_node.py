""" 
Python program find and return data stored in the nth index of the linked list
"""

class Node:

    """ 
    constructor to initialize the Node
    """
    def __init__(self, data=None):
        self.data = data # -----------------------> 0(1)
        self.next = None # -----------------------> 0(1)



class LinkedList:    

    """ 
    Contructor to initialize the head node
    """
    def __init__(self) -> None:
        self.head = None # ----------------------------------> O(1)

    
    def format_console(self):
        print(f"===============================================================================================")


    """ 
    function to show all the data stored the created linked list
    """    
    def print_list(self):
        current_node = self.head # -----------------------> 0(1)

        while(current_node): # -----------------------> 0(n)
            print(current_node.data, end=" ") # -----------------------> 0(1)
            current_node = current_node.next # -----------------------> 0(1)
        
        print("\n") # -----------------------> 0(1)


    """ 
    function to add new node at the begining of the linked list 
    """
    def push(self, new_data):

        # create a new node and initialize with new data
        new_node = Node(new_data) # -----------------------> 0(1)


        # Link the next of the new node to the head node
        new_node.next = self.head # -----------------------> 0(1)

        # make the new node ad the head node
        self.head = new_node # -----------------------> 0(1)


    """ 
    funtion to find the data in the nth node
    """
    def find_nth_node(self, index):

        current_node = self.head # -----------------------> 0(1)
        count = 0 # initialize the node count as 0
        while(current_node): # -----------------------> 0(n)
            if index == count: # -----------------------> 0(1)
                return f"The data found at the node index-->{index} is {current_node.data}" # -----------------------> 0(1)
            current_node = current_node.next # -----------------------> 0(1)
            count += 1 # -----------------------> 0(1)
        
        # if the provided index does not exist, assert as false
        # assert(False)
        return f"No Node with the given index found." # -----------------------> 0(1)



""" 
Object creation and function calls
"""

linked_list = LinkedList()

for i in range(1, 5):
    linked_list.push(i)

linked_list.format_console()
print(f"The Data stored in the created linked list as follows: ", end=" ")
linked_list.print_list()

result = linked_list.find_nth_node(10)
linked_list.format_console()
print(result)
    
