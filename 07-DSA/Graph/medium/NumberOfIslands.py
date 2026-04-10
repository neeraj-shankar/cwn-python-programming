"""
Given a matrix of integers A of size N x M consisting of 0 and 1. A group of connected 1's forms an island.
From a cell (i, j) such that A[i][j] = 1 you can visit any cell that shares a corner with (i, j) and
value in that cell is 1.

More formally, from any cell (i, j) if A[i][j] = 1 you can visit:

(i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
(i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
(i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
(i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
(i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
(i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
(i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
(i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.
Return the number of islands.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.

"""
import sys

sys.setrecursionlimit(1000000)

class NumberOfIslands:

    def solution_dfs(self, matrix: list[list[int]]):
        """
        1. Create a Visited array to track unvisited nodes
        2. Since diagaonal elements are also include, create direction array of 8 directions
        3. Traverse the matrix if any cell is 1 and its not visited, increase count by one.
        4. Then call the dfs method for current cell.
        """
        n = len(matrix)
        m = len(matrix[0])

        visited = [[False] * m for _ in range(n)]

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]

        count = 0
        for i in range(0, n):
            for j in range(0, m):

                if matrix[i][j] == 1 and not visited[i][j]:
                    count += 1
                    self.dfs(matrix, i, j, directions, visited)
        return count

    def dfs(
        self,
        matrix: list[list[int]],
        i: int,
        j: int,
        directions: list[tuple[int]],
        visited: list[list[int]],
    ):
        """
        1. Mark the current cell as visited
        2. Check in all directions, if any cell is 1 and not its visited.
        3. call dfs for the new cell.
        4. Always check if the current cell to be explored is inside matrix
        """
        visited[i][j] = True
        for dx, dy in directions:
            nr = i + dx
            nc = j + dy
            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):

                if matrix[nr][nc] == 1 and not visited[nr][nc]:
                    self.dfs(matrix, nr, nc, directions, visited)


if __name__ == "__main__":

    noi = NumberOfIslands()

    A = [[1, 1, 0, 0, 0],[0, 1, 0, 0, 0], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1]]
    print(f"Total Islands: {noi.solution_dfs(A)}")
