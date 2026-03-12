"""
Implement the next permutation, which rearranges numbers into the numerically next greater permutation
of numbers for a given array A of size N.

If such arrangement is not possible, it must be rearranged as the lowest possible order,
i.e., sorted in ascending order.

NOTE:
The replacement must be in-place, do not allocate extra memory.
DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION. Use of Library functions will disqualify your
submission retroactively and will give you penalty points.
"""


class NextPermutation:

    def solution_bruteforce(self, A):
        pass

    def solution_swap_and_sort(self, A):
        """
        1. Traverse from back and find the first dipping element.
        2. Use the index of dipping element to swap it with just greater element.
        3. reverse the element from index + 1 to till end
        """
        n = len(A)

        # Find First Dipping element
        idx = n - 2
        while idx >= 0 and A[idx] >= A[idx + 1]:
            idx -= 1

        # Swap with just larger element
        for i in range(n - 1, idx, -1):

            if A[i] > A[idx]:
                A[i], A[idx] = A[idx], A[i]
                break

        # Reverse the array from idx + 1 to n-1
        self.reverse(A, idx + 1, n - 1)

        return A

    def reverse(self, nums: list, start: int, end: int) -> None:
        pass


if __name__ == "__main__":

    np = NextPermutation()

    # Test Case 1:
    A = [1, 2, 3]
    print(f"Next greater permutation: {np.solution_swap_and_sort(A)}")
