"""
You are given a matrix A of integers of size N × M consisting only of 0s and 1s.
For each cell of the matrix, find the distance to the nearest cell containing 1.
"""

from collections import deque


class Pair:

    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = 0


class NearestOnes:

    def solution(self, A):
        """
        Algorithm
        -----------------------------------------
        1. Create a pair class with row, col and dist as attributes
        2. Travel through the matrix A and add all the cell containing 1 to a queue
        3. Now while queue size is greater than 0:
            a. remove the current Pair
            b. get new cell coordinate using direction array, update its value by +1
            c. add the new cell to the queue
        """

        n = len(A)
        m = len(A[0])
        # Create a queue to store sources
        q = deque()

        # Update the cell value of
        for i in range(0, n):

            for j in range(0, m):
                if A[i][j] == 1:
                    q.append(Pair(i, j, 0))
                    A[i][j] = 0
                else:
                    A[i][j] = -1

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        while len(q) > 0:
            # Remove
            rem = q.popleft()
            r = rem.row
            c = rem.col

            # Process
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if nr >= 0 and nr < n and nc >= 0 and nc < m and A[nr][nc] == -1:
                    # update the new cell value
                    A[nr][nc] = A[r][c] + 1
                    q.append(Pair(nr, nc, A[r][c] + 1))

        return A


if __name__ == "__main__":

    no = NearestOnes()

    A = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 0]]
    print(no.solution(A))  # [[3, 2, 1, 0], [2, 1, 0, 0], [1, 0, 0, 1]]

    # Test case 2:  ones at corners
    A = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
    print(no.solution(A))  # [[0, 1, 2], [1, 2, 1], [2, 1, 0]]

    # Test Case 3: Large Zero Region
    A = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
    print(no.solution(A))  # [[2, 3, 4, 5], [1, 2, 3, 4], [0, 1, 2, 3]]

    # Test Case 4: Single 1 in matrix
    A = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(no.solution(A))  # [[2, 1, 2], [1, 0, 1], [2, 1, 2]]

    # Test Case 5: All 1's
    A = [[1, 1], [1, 1]]
    print(no.solution(A))  # [[0, 0], [0, 0]]

    # Test Case 6: One column matrix
    A = [[0], [1], [0], [0]]
    print(no.solution(A))
