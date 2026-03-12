"""
Given a matrix of integers A of size N x M consisting of 0, 1 or 2.

Each cell can have three values:

1. The value 0 representing an empty cell.
2. The value 1 representing a fresh orange.
3. The value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.

Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.

"""

from collections import deque


class Pair:

    def __init__(self, row: int, col: int, time: int):

        self.row = row
        self.col = col
        self.time = time


class RottenOranges:

    def solution(self, A):
        """
        Using a direction array, move across all four sides,
        """
        # Total rows and columns in A
        n = len(A)
        m = len(A[0])

        # Create direction array to travel across neighbours
        dr = [-1, 0, 1, 0]  # TLBR
        dc = [0, -1, 0, 1]  # TLBR

        # Create a queue and add the the rotten oranges to it.
        q = deque()

        for i in range(0, n):
            for j in range(0, m):
                if A[i][j] == 2:
                    q.append(Pair(i, j, 0))

        # Remove, process, and add neighbours
        min_time = 0
        while len(q) > 0:

            # Remove
            rem = q.popleft()

            # Process
            row = rem.row
            col = rem.col
            t = rem.time
            min_time = t
            for d in range(0, 4):
                nr = row + dr[d]
                nc = col + dc[d]

                if nr >= 0 and nc >= 0 and nr < n and nc < m and A[nr][nc] == 1:
                    A[nr][nc] = 2  # Rot the fresh orange

                    # Add this rotten cell to the queue
                    q.append(Pair(nr, nc, t + 1))

        # Finally, verify whether any orange exists that is not rotten

        for i in range(0, n):
            for j in range(0, m):
                if A[i][j] == 1:
                    return -1

        return min_time


if __name__ == "__main__":

    ro = RottenOranges()

    # Test case 1: Single rotten cell
    A = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(f"Min time to rot all oranges: ", ro.solution(A))

    # Test Case 2: Not possible to rot all
    A = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(f"Min time to rot all oranges: ", ro.solution(A))

    # Test Case 3: 
    A = [[0,2,1],[2,2,1],[0,1,0],[2,1,1],[0,1,1],[1,2,1]]
    print(f"Min time to rot all oranges: ", ro.solution(A))


