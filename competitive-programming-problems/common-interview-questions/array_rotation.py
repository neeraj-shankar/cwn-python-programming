"""
Rotating a given array elements by user provided factor
"""


class ArrayRotation:

    def __init__(self, input_data, factor) -> None:

        self.input_data = input_data
        self.factor = factor

    def rotate_array_temporary(self):
        """
        Copy the last k elements of the array into a temporary array,
        shift the remaining elements to the right, and then copy the
        temporary array back to the beginning.
        """
        n = len(self.input_data)

        # Handle cases where k is greater than the length of the array
        k = self.factor % n

        # list of last k elements of the array into a temporary array
        temp = self.input_data[n - k :]
        print(f"Temp Array: {temp}")

        # Traverse from end the list to rotation pivot index
        # shift the element to the right
        for i in range(n - 1, k - 1, -1):
            print(f"Index Number: {i}")
            self.input_data[i] = self.input_data[i - k]
        # Copy the temporary array back to the beginning.
        self.input_data[:k] = temp


if __name__ == "__main__":

    raw_data = [0, 1, 2, 4, 5, 6]
    rotating_factor = 3

    result = ArrayRotation(raw_data, rotating_factor).rotate_array_temporary()
    print(f"Original Array: {raw_data}")
    print(f"Array after rotated by factor {rotating_factor}: {result}")
