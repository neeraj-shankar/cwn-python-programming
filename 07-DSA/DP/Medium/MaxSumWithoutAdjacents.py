"""
/*
Given a 2 x N grid of integers, A, your task is to choose numbers from the grid such that sum of these
numbers is maximized.

However, you cannot choose two numbers that are adjacent horizontally, vertically, or diagonally.

Return the maximum possible sum.

Note: You are allowed to choose more than 2 numbers from the grid.

*/
"""


class MaxSumWithoutAdjacents:

    def solution_tda(self, matrix: list[list[int]]):
        """
        Algorithm Design
        -----------------------------------------------------------------------
        1. Convert the 2D array into 1D by taking maximum element from each column.
        2. Call for the classic house robber problem
        """

        # Edge case 1: Empty list or sub list

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        # Edge Case 2: Single column in matrix
        if len(matrix[0]) == 1:

            return max(matrix[0][0], matrix[1][0])

        # Generic Case:
        # 1. Convert the 2d into 1d with max from each column
        m = len(matrix[0])
        max_elements = [0] * m
        for i in range(m):

            max_elements[i] = max(matrix[0][i], matrix[1][i])

        print(max_elements)
        memo = [-1 for _ in range(m)]
        return self.house_robber(max_elements, 0, memo)

    def house_robber(self, nums: list[int], idx: int, memo: list[int]):
        print(F"I am being called for {idx} where n is {len(nums)}")
        # Base Case:
        if idx >= len(nums):
            return 0

        if memo[idx] != -1:
            return memo[idx]
        
        # Pick call 
        pick = self.house_robber(nums, idx+2, memo) + nums[idx]

        # Skip call 
        skip = self.house_robber(nums, idx+1, memo)

        memo[idx] = max(pick, skip)
        return memo[idx]

if __name__ == "__main__":

    mswa = MaxSumWithoutAdjacents()

    # Test Case 1:
    A = [[1, 2, 3, 4], [2, 3, 4, 5]]
    print(mswa.solution_tda(A))
