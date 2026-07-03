"""
You are given an array A of integers that represent the lengths of ropes.

You need to connect these ropes into one rope. The cost of joining two ropes equals the sum of their lengths.

Find and return the minimum cost to connect these ropes into one rope.
"""

class ConnectingRopes:

    def solution_sorting(A: list[int]) -> int:
        """
        Algorithm Design
        ---------------------------------------------------
        1. Sort the array, take and remove first two smallest element
        2. Add them and put back in the array.
        3. Repeat 1 and 2 till only single element is left

        -------------------------------
        Time Complexity: O(n * nlogn)
        Space Complexity: O(n)
        """

        n = len(A)
        A.sort()
        total_cost = 0
        # Remove first and second element
        while len(A) > 1:
            r1 = A.pop(0)
            r2 = A.pop(0)
            nr = r1 + r2 
            total_cost += nr 
            A.append(nr) 
            A.sort()
            print(A)
        print(total_cost)


if __name__ == "__main__":

    cr = ConnectingRopes()

    # Test Case 1:
    A = [2, 5, 2, 6, 3]
    ConnectingRopes.solution_sorting(A)    