""" 
Python program to demonstrate the searching of an element in the linked list
"""

class Node:
    # function to initialize the Node data and address field
    def __init__(self, data=None):
        self.my_data = data
        self.next = None


class SearchElement:

    # Create and initialize the head node
    def __init__(self):
        self.head = None

    # function to print the data stored in the linked list    
    def print_list(self):

        # check if the list is empty
        if self.head == None:
            return f"The Linked List is empty."
        
        temp = self.head
        while(temp):
            print(temp.my_data, end=" ")
            temp = temp.next
        print("\n")

    def push(self, new_data):

        # create a new node and initialize the head
        new_node = Node(new_data)

        # Make the new node next as head of the linked list
        new_node.next = self.head

        # finally, make the new node as head node
        self.head = new_node

    # function to find element from a given linked list
    def find_element(self, element):
        temp = self.head

        while(temp):
            if temp.my_data == element:
                return True
            temp = temp.next
        return False

    # def search_using_recurrsion(self, linked_list, element):

    #     # Check for base case
    #     if self.head == None:
    #         return False
        
    #     return search_using_recurrsion(linked_list.head, 3)
        



""" 

"""
linked_list = SearchElement()
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)

print(linked_list.print_list())
print(linked_list.find_element(7))