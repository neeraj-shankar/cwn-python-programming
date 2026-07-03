"""
You are given a 2D matrix cost of size N × M, where each cell contains a non-negative integer representing the cost 
of stepping on that cell.

A robot starts at the top-left cell (0,0) and needs to reach the bottom-right cell (N-1, M-1).

From any cell (i, j), the robot can move only in the following directions:
1. Right → (i, j + 1)
2. Down → (i + 1, j)
3. Diagonal → (i + 1, j + 1)

The cost of a path is defined as the sum of the values of all cells visited, including the source and destination cells.
Your task is to find the minimum possible cost required to reach the destination.

Follow-up
------------------------------------------
Can you also return the actual path (sequence of coordinates) that yields the minimum cost instead of only 
returning the minimum cost?
"""

class MinCostPath:

    def solution_tda(self, matrix:list[list[int]]):

        n = len(matrix)
        m = len(matrix[0])
        memo = [[-1] * m for _ in range(n)]
        print(memo)

        ans = self.minCost(matrix, 0, 0, memo)
        return ans

    def minCost(self, matrix: list[list[int]], i: int, j: int, memo: list[list[int]]):
        """
        Algo Design
        -----------------------------------------
        1. 
        """

        # Base Case 1: Reached destination
        if i == len(matrix)-1 and j == len(matrix[0]) - 1:
            return matrix[i][j]
        
        # Invalid Case: Outside matrix
        if i == len(matrix) or j == len(matrix[0]):
            return float('inf')
        
        # Before making call, check if minpath already computed
        if memo[i][j] != -1:
            return memo[i][j]
        
        right = self.minCost(matrix, i, j+1, memo)
        down = self.minCost(matrix, i+1, j, memo)
        diagonal = self.minCost(matrix, i+1, j+1, memo)

        best = min(diagonal, min(right, down))
        memo[i][j] = matrix[i][j] + best

        return memo[i][j]

if __name__ == "__main__":

    mcp = MinCostPath()

    # Test Case 1
    cost =[[1, 2, 3], [4, 8, 2],[1, 5, 3]]
    print(f"Minimum cost: {mcp.solution_tda(cost)}")

