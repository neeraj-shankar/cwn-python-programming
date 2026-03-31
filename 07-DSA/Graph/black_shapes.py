"""
Given character matrix A of dimensions N×M consisting of O's and X's, where O = white, X = black.

Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)

Problem Constraints
-------------------------------------------------
1 <= N, M <= 1000
A[i][j] = 'X' or 'O'

Input Format
-------------------------------------------------
The First and only argument is character matrix A.

Output Format
-------------------------------------------------
Return a single integer denoting number of black shapes.
"""


class BlackShapes:

    def solution_dfs(self, matrix: list[list[int]]) -> int:
        """
        Algorithm
        -----------------------------------------
        1. Traverse every cell
        2. If encountered an 'X' that is not visited yet, new shape is found.
        3. Call for dfs method, mark all its neighbour as visited
        """

        n, m = len(matrix), len(matrix[0])

        # Create visited array for each cell
        visited = [[False] * m for _ in range(n)]

        # Create direction array to travel across all for sides - TLDR
        dr = [-1, 0, 1, 0]
        dc = [0, -1, 0, 1]

        # For each cell, check and call dfs
        count = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "X" and visited[i][j] == False:
                    self.dfs(matrix, i, j, n, m, visited, dr, dc)
                    count += 1

        return count

    def dfs(
        self,
        matrix: list[list[int]],
        r: int,
        c: int,
        n: int,
        m: int,
        visited: list[int],
        dr: list[int],
        dc: list[int],
    ):

        # Discard invalid moves - out of matrix, cell value is not 'X'
        if r < 0 or c < 0 or r >= n or c >= m:
            return

        if matrix[r][c] != "X" or visited[r][c] == True:
            return

        visited[r][c] = True
        for x in range(4):
            nr = r + dr[x]
            nc = c + dc[x]
            self.dfs(matrix, nr, nc, n, m, visited, dr, dc)


if __name__ == "__main__":

    bs = BlackShapes()

    # Test Case 1:
    A = ["XOX", "OXO", "XOX"]
    print("Total black shapes found: ", bs.solution_dfs(A))

    # Test Case 2:
    A = ["XXOO", "XXOO", "OOXX", "OOXX"]
    print("Total black shapes found: ", bs.solution_dfs(A))

    # Test Case 3:
    A = ["XOO", "OXO", "OOX"]
    print("Total black shapes found: ", bs.solution_dfs(A))

    # Test Case 4:
    A = ["XOOOX", "XXOOX", "OOXXX", "OXOOO", "XOXOX"]
    print("Total black shapes found: ", bs.solution_dfs(A))
