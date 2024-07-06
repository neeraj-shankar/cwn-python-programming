"""
Problem Statemen:
-------------------------------------------------------------------------------
Here is a situation where we want to remove the duplicates from an array (list)
which is sorted already. 
-------------------------------------------------------------------------------
"""

class DuplicateElmination:

    def __init__(self, input_data) -> None:
        
        self.input_data = input_data


    def remove_duplicate_item_two_pointers(self):

        """
        Iterate through the array with two pointers: one to keep track of the 
        current position and another to iterate ahead to find unique elements.
        Shift unique elements to the front of the array.

        """

        if not self.input_data:
            return []
        
        j = 0 # Keeps track of the current position
        for i in range(1, len(self.input_data)):

            if self.input_data[i] != self.input_data[j]:

                j += 1
                self.input_data[j] = self.input_data[i]

        return self.input_data[:j + 1]
        
if __name__ ==  "__main__":

    raw_data = [1, 2, 2, 3, 4, 4, 7, 7, 7, 8, 8]

    result = DuplicateElmination(raw_data).remove_duplicate_item_two_pointers()
    print(f" The Array after duplicates removed: {result}")
