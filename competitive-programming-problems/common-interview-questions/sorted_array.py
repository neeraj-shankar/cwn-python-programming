"""
An array is said to be sorted in non-decreasing order if each element in the array is less than or equal to the next element. 
In other words, the elements of the array are arranged in ascending order, but the array can contain duplicate elements.
"""

class SortedArray:

    def __init__(self, input_data) -> None:
        self.input_data = input_data

    def is_sorted_iterative(self):

        n = len(self.input_data)
        for i in range (n-1):
            if self.input_data[i] > self.input_data[i + 1]:
                return False
        
        return True
    
    def is_sorted_all(self):

        n = len(self.input_data)

        return all(self.input_data[i] <= self.input_data[i + 1] for i in range(n-1))
    

if __name__ == "__main__":
    raw_data = [1, 1, 2, 3, 3, 3, 4, 4] # Is the Array sorted in non-decreasing order: True
    raw_data = [1, 1, 2, 3, 5, 3, 4, 4] # Is the Array sorted in non-decreasing order: False

    result = SortedArray(raw_data).is_sorted_iterative()
    print(f"Is the Array sorted in non-decreasing order: {result}")

    result = SortedArray(raw_data).is_sorted_all()
    print(f"Is the Array sorted in non-decreasing order: {result}")