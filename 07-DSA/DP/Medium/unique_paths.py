"""
 There is a robot on an m x n grid. The robot is initially located at the top-left corner 
 (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 

The robot can only move either down or right at any point in time.
 
Given the two integers m and n, return the number of possible unique paths that the robot can take to 
reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""

class UniquePaths():

    def solution_baa(self, m: int, n: int) -> int:

        # Create a dp array of size m * n to store computed result
        dp = [[-1] * n for _ in range(m)]
        print(dp)

        # Mark all first column each row as 1: Travel through rows
        for row in range(m):
            dp[row][0] = 1

        # Mark first row in each column as 1: Move through columns
        for col in range(n):
            dp[0][col] = 1

        for i in range(1, m):
            for j in range(1, n):

                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        print(f"Final DP:\n{dp}")
        return dp[m-1][n-1]

if __name__ == "__main__":

    up = UniquePaths()

    # Test Case 1: Square Matrix
    print(f"Total number of  paths: {up.solution_baa(4, 4)}")