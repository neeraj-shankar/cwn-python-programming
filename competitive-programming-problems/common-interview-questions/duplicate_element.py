"""
Determine if there are any duplicates in an array.
"""
import collections

from collections import  Counter


class DuplicateElement:

    def __init__(self, data):
        self.data = data

    def has_duplicates_iterative(self):
        """
        Sort the array first and then iterate through it, checking if
        adjacent elements are equal.
        """
        self.data.sort()
        for i in range(len(self.data) - 1):
            if self.data[i] == self.data[i + 1]:
                return True
        return False

    def duplicate_element_dict(self):
        """
         uses a Counter object from the collections module to count the
         occurrences of each element in the array. If any count is greater
         than 1, it means there is a duplicate.
        """
        count = {}
        for element in self.data:
            count[element] = count.get(element, 0) + 1

        return any(c > 1 for c in count.values())

    def has_duplicates_set(self):
        """
         converts the array to a set and compare the lengths. If the
         length of the set is less than the length of the array, it means
         there are duplicates.
        """
        new_set = set(self.data)
        if len(self.data) > len(new_set):
            return True
        return False

    def has_duplicates_counter(self):
        """
        uses a Counter object from the collections module to count the
        occurrences of each element in the array. If any count is greater
        than 1, it means there is a duplicate.
        """

        element_counts = Counter(self.data)

        return any(count > 1 for count in element_counts.values())


if __name__ == "__main__":

    raw_data = [1, 3, 2, 7, 9, 2, 5]

    result = DuplicateElement(raw_data).has_duplicates_iterative()
    print(f"Does this array contain any duplicate: {result}")

    result = DuplicateElement(raw_data).duplicate_element_dict()
    print(f"Does this array contain any duplicate: {result}")

    result = DuplicateElement(raw_data).has_duplicates_set()
    print(f"Does this array contain any duplicate: {result}")
    result = DuplicateElement(raw_data).has_duplicates_counter()
    print(f"Does this array contain any duplicate: {result}")

