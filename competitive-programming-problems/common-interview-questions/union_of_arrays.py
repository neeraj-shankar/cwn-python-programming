"""
Find the union of two arrays.
-----------------------------------------------------------------------
The union of two sets X and Y is equal to the set of elements that are 
present in set X, in set Y, or in both the sets X and Y.
"""
from collections import Counter


class ArraysUnion:

    def __init__(self, input_data_first, input_data_second) -> None:

        self.input_data_first = input_data_first
        self.input_data_second = input_data_second

    def union_list_concatenation(self):
        """
        Concatenate both arrays into a single list and then convert it
        to a set to remove duplicates.

        """

        return list(set(self.input_data_first + self.input_data_second))
    
    def union_list_comprehension(self):

        """
        Iterate through both arrays and add elements to a new list if
        they are not already present.
        """

        union_list = [x for x in self.input_data_first + self.input_data_second if x not in self.input_data_first or self.input_data_second]

        return union_list
    
    def union_list_union_method(self):

        """
        Convert both arrays to sets and then perform set union.
        """

        union_list = list(set(self.input_data_first).union(set(self.input_data_second)))
        return union_list

    def union_counter(self):
        counter1 = Counter(self.input_data_first)
        print(counter1)
        counter2 = Counter(self.input_data_second)
        print(counter1.elements)
        return list((counter1 | counter2).elements())

        



if __name__ == "__main__":

    raw_data_first = [1, 2, 3, 4, 5]
    raw_data_second = [4, 5, 6, 7, 8]

    result = ArraysUnion(raw_data_first, raw_data_second).union_list_concatenation()
    print(f"The Union of two arrays: {result}")

    result = ArraysUnion(raw_data_first, raw_data_second).union_list_comprehension()
    print(f"The Union of two arrays: {result}")

    result = ArraysUnion(raw_data_first, raw_data_second).union_list_union_method()
    print(f"The Union of two arrays: {result}")

    result = ArraysUnion(raw_data_first, raw_data_second).union_counter()
    print(f"The Union of two arrays: {result}")
