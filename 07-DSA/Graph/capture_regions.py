"""
Given a 2-D board A of size N x M containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""

from collections import deque


class Pair:

    def __init__(self, row, col):
        self.row = row
        self.col = col


class CaptureRegion:

    def solution_bfs(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        Algorithm
        ---------------------------------------------------
        1. First go and mark all the 'O' on boundary as Safe. They cannot be captured
        2. Add all the Safe cell to the queue and do the following:
            a. remove it, look in all four direction and mark any '0' it touches as safe.
            b. Add that cell to the queue.

        """
        n = len(matrix)
        m = len(matrix[0])

        q = deque()
        # Travel across row and column. Mark all the boundary o as safe
        # And add to them to the queue
        for i in range(0, n):
            for j in range(0, m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    if matrix[i][j] == "O":
                        matrix[i][j] = "S"
                        q.append(Pair(i, j))

        print(matrix)
        print(q)

        dr = [1, 0, -1, 0]
        dc = [0, 1, 0, -1]
        # Traverse the
        while len(q) > 0:

            # Remove
            rem = q.popleft()

            for d in range(4):
                nr = rem.row + dr[d]
                nc = rem.col + dc[d]

                if (nr >= 0 and nr < n - 1 and nc >= 0 and nc < m - 1 and matrix[nr][nc] == "O"):
                    matrix[nr][nc] = "S"
                    q.append(Pair(nr, nc))


        for i in range (n):
            for j in range(m):
                if matrix[i][j] == "O":
                    matrix[i][j] = "X"
                elif matrix[i][j] == 'S':
                    matrix[i][j] = "0"

        return matrix

if __name__ == "__main__":
    cr = CaptureRegion()

    A = [["X", "O", "O"], ["X", "O", "X"], ["O", "O", "O"]]
    print("Ans: ", cr.solution_bfs(A))

    A = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    print("Ans: ", cr.solution_bfs(A))
