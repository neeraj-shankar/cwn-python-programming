"""
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

1. The elements of the first array are all factors of the integer being considered
2. The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

Problem breakdown
---------------------------
Array A, where all elements are factors of a certain integer "X."
Array B, where all elements are multiples of the same integer "X."
The task is to find how many different values of "X" exist such that:

All elements in Array A are factors of X. --> All the number should completely divide X
X is a factor of all elements in Array B. --> X should be able to divide all the numbers in array.
"""


class NumberInBetween:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def getTotalX(self):
        count = 0

        for x in range(max(self.arr1), min(self.arr2) + 1):
            if all(x % num_a == 0 for num_a in self.arr1) and all(
                num_b % x == 0 for num_b in self.arr2
            ):
                count += 1

        return count


if __name__ == "__main__":
    array_a = [2, 4]
    array_b = [16, 32, 96]

    result = NumberInBetween(array_a, array_b).getTotalX()
    print(result)  # Output: 3 (X values 4, 8, and 16 satisfy the conditions)
