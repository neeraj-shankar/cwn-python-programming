"""
Find the maximum and minimum elements in an array.
"""


class MaxMinElement:

    def __init__(self, input_data) -> None:
        self.input_data = input_data

    def find_max_min_loop(self):

        if not self.input_data:
            return None

        max_element = min_element = self.input_data[0]
        for num in self.input_data:
            if num > max_element:
                max_element = num
            elif num < min_element:
                min_element = num
        return max_element, min_element


if __name__ == "__main__":

    raw_data = [3, 7, 19, 14, 2]

    result = MaxMinElement(raw_data).find_max_min_loop()
    print(f"Max and Min Element in order: {result}")