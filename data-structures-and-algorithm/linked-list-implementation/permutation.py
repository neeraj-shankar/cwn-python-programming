""" 
Python program to find out if two python list are permutation of each other
"""

class PermuationCheck:

    """ 
    function to determine if two lists are permutation of each other
    """
    def permutation(self, list1, list2):

        # base case check 
        if len(list1) != len(list2):
            return False
        
        # Main Case - validation 
        list1.sort()
        list2.sort()

        if list1 == list2:
            return True
        else:
            return False


""" 
Object Creation and function calls
"""
list1 = [1, 2, 3]
list2 = [2, 1, 4]
permutation_check = PermuationCheck()
result = permutation_check.permutation(list1=list1, list2=list2)
print(result)