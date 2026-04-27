"""
Find the longest increasing subsequence of a given array of integers, A.

In other words, find a subsequence of array in which the subsequence's elements are in strictly 
increasing order, and in which the subsequence is as long as possible.

In this case, return the length of the longest increasing subsequence.

Problem Constraints
---------------------------------------------------------------------
1 <= length(A) <= 2500
0 <= A[i] <= 2500
"""

class LongestIncSubsequence:

    def solution_tda(self, A: list[int]):
        """
        1. Explore all the subsequence where previous element is less than current element.
        """
        n = len(A)

        memo = []

        return self.subset(A, -1, 0, memo)

    def subset(self, nums: list[int], prev: int, idx: int, memo: list[int]):

        # Base Case:
        if idx == len(nums):
            return 0
        
        # Skip call
        skip = self.subset(nums, prev, idx+1, memo)

        # Pick call
        pick = 0
        if prev == -1 or nums[prev] < nums[idx]:
            pick = 1 + self.subset(nums, idx, idx+1, memo)

        return max(pick, skip)

if __name__ == "__main__":

    ls = LongestIncSubsequence()

    # Test Case 1: 
    A = [1, 2, 1, 5]
    print(f"Longest Increasing Subsequence: {ls.solution_tda(A)}")