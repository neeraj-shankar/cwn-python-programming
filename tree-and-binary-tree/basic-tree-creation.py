""" 
Python program to demonstrate the creation of basic tree using python
"""

class TreeNode:

    """ 
    Constructor to initialize the data and child node
    """
    def __init__(self, data, children = []):
        self.tree_data = data
        self.tree_children = children

    """ 
    str function to print the data of the tree structure
    """
    def __str__(self, level=0):
        ret = " " + level + str(self.tree_data) + "\n"
    
        for child in self.tree_children:
            ret += child.__str__(level + 1)
        
        return ret
    
    