"""
Given a matrix of integers A of size N x M and an integer B.

In the given matrix every row and column is sorted in non-decreasing order.
Find and return the position of B in the matrix in the given form:
If A[i][j] = B then return (i * 1009 + j)
If B is not present return -1.

Note 1: Rows are numbered from top to bottom and columns are numbered from left to right.
Note 2: If there are multiple B in A then return the smallest value of i*1009 +j such that A[i][j]=B.
Note 3: Expected time complexity is linear
Note 4: Use 1-based indexing
"""


class MatrixSearch:

    def solution_bruteforce(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        1. Traverse each cell of the matrix and compare.
        2. If current cell value equals the target return: i * 1009 + j
        """
        pass

    def solution_optimal(self, matrix: list[list[int]], target: int) -> int:
        """
        1. Start from TR corner of the matrix (r=0, c=m-1).
        2. If current cell value is less than target, move downwards
        3. If current cell value is greater, move leftwards

        Time and space Complexity
        -------------------------------
        """

        n = len(matrix)
        m = len(matrix[0])

        r = 0
        c = m - 1
        ans = float('inf')
        while r < n and c >= 0:

            if matrix[r][c] == target:
                print(f"Target found at ({r}, {c})")
                pos = (r+1) * 1009 + (c+1)
                ans = min(ans, pos)
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1

        return -1 if ans == float('inf') else ans


if __name__ == "__main__":

    ms = MatrixSearch()

    # Test case 1:
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = 2
    print(f"The position of the target: {ms.solution_optimal(A, B)}")

