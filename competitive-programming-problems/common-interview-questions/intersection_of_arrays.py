"""
Find the intersection of two arrays.
"""


class InersectingArrays:

    def __init__(self, input_data_first, input_data_second) -> None:

        self.input_data_first = input_data_first
        self.input_data_second = input_data_second

    def find_intersection_sets(self):
        """
        Convert both arrays to sets and then perform set intersection.
        """

        array_set_first = set(self.input_data_first)
        array_set_second = set(self.input_data_second)

        return array_set_first.intersection(array_set_second)

    def find_intersection_list_comprehension(self):
        """
        Iterate through one array and check if each element is present in the
        other array.

        """

        intersected_array = [
            x for x in self.input_data_first if x in self.input_data_second
        ]

        return intersected_array

    def find_intersection_filter(self):
        """
        Use the filter() function to filter elements from one array based on
        their presence in the other array.
        """

        intersected_array = list(
            filter(lambda x: x in self.input_data_first, self.input_data_second)
        )

        return intersected_array


if __name__ == "__main__":

    raw_data_first = [1, 2, 3, 4, 5]
    raw_data_second = [4, 5, 6, 7, 8]

    result = InersectingArrays(raw_data_first, raw_data_second).find_intersection_sets()
    print(f"The Intersection of two given array: {result}")

    result = InersectingArrays(
        raw_data_first, raw_data_second
    ).find_intersection_list_comprehension()
    print(f"The Intersection of two given array: {result}")

    result = InersectingArrays(
        raw_data_first, raw_data_second
    ).find_intersection_filter()
    print(f"The Intersection of two given array: {result}")
