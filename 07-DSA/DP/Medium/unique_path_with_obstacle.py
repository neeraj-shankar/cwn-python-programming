"""
Given a grid of size n * m, lets assume you are starting at (1,1) and your goal is to reach (n, m).
At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).

Now consider if some obstacles are added to the grids.
Return the total number unique paths from (1, 1) to (n, m).

Note:
1. An obstacle is marked as 1 and empty space is marked 0 respectively in the grid.
2. Given Source Point and Destination points are 1-based index.
"""


class UniquePathsII:

    def solution_tda(self, A: list) -> int:
        n = len(A)
        m = len(A[0])
        dp =[[-1] * m for _ in range(n)]

        return self.paths(A, n-1, m-1, dp);

    def paths(self, A: list[int], row: int, col: int, dp: list[list[int]]):


        # Went outside matrix
        if ( row < 0 or col < 0): 
            return 0
        
        # Hit an obstacle
        if (A[row][col] == 1):
            return 0
        
        # Path found
        if (row == 0 and col == 0):
            dp[row][col] = 1
            return 1
        
        # Check dp table before making call
        if dp[row][col] != -1:
            return dp[row][col]
        
        # Go horizontal and give the result
        from_horizontal = self.paths(A, row, col-1, dp)

        # Go vertical and give result
        from_vertical = self.paths(A, row-1, col, dp)
        
        dp[row][col] = from_horizontal + from_vertical
        return dp[row][col]



    def solution_tabular_dp(self, A: list) -> int:

        rows = len(A)
        cols = len(A[0])
        # Create a 2d array for store the results
        dp = [[-1] * cols for _ in range(rows)]

        # Base case: If obstacle is at start or end
        if A[0][0] == 1 or A[rows - 1][cols - 1] == 1:
            return 0

        # Base case 2: Fill cell with 1
        dp[0][0] = 1

        # Fill the first rows by inheriting from previous col
        # only way to reach is from left side
        for col in range(1, cols):
            if A[0][col] == 1:
                dp[0][col] = 0  # The obstacle problem
            else:
                dp[0][col] = dp[0][col - 1]

        # Fill the first column by inherting from previos row
        # only way to reach is from top
        for row in range(1, rows):
            if A[row][0] == 1:
                dp[row][0] = 0
            else:
                dp[row][0] = dp[row - 1][0]

        # Fill the all remaining cases
        for row in range(1, rows):
            for col in range(1, cols):

                if A[row][row] == 1:
                    dp[row][col] = 0  # The obstacle problem
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        print(f"Final Computed DP Table:\n {dp}")

        return dp[rows - 1][cols - 1]


if __name__ == "__main__":

    up2 = UniquePathsII()

    A = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(f"Total Unique Paths using recursive approach: {up2.solution_tda(A)}")
    print(f"Total Unique Paths using iterative approach: {up2.solution_tabular_dp(A)}")

    # Test case 2: No path found
    A = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    print(f"Total Unique Paths using recursive approach: {up2.solution_tda(A)}")
    print(f"Total Unique Paths using iterative approach: {up2.solution_tabular_dp(A)}")

