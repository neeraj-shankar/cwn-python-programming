"""
Given an array A of length N, your task is to find the maximum possible sum of any non-empty contiguous 
subarray.

In other words, among all possible subarrays of A, determine the one that yields the highest sum 
and return that sum.
"""

class MaximumSubarraySum():

    def solution_bruteforce(self, A: list) -> int:
        """
        1. Generate  all subarrays, find sum of each subarray.
        2. Compare and track subarray with maximum sum

        Time and Space Complexity
        ---------------------------------------------------
        TC: O(N^3) and SC: O(1)
        """

        ans = float('-inf')

        # Length of the array
        n = len(A)
        for i in range(0, n):
            for j in range(i, n):
                total = 0
                for k in range(i, j+1):
                    total += A[k]

                print(f"Current subarray sum: {total}, indexed from {i} to {j}")
                ans = max(ans, total)

        return ans
    
    def solution_kadane(self, A):
        """
        1. Traverse through array in one pass
        2. for sum > 0, take contribution of the current element.
        3. Check and update max
        4. if sum < 0, discard the current subarray and start from new index.
        """

        max_sum = float('-inf')
        current_sum = 0
        for num in A:
            current_sum += num 

            if max_sum < current_sum:
                max_sum = current_sum

            if current_sum < 0:
                current_sum = 0
        return max_sum

if __name__ == "__main__":

    mss = MaximumSubarraySum()

    # Test Case 1: 
    A = [1, 2, 3, 4, -10]
    result = mss.solution_kadane(A)
    print(f"Maximum Subarray Sum Bruteforce: {result}")

    # Test case 2: decreasing negatives
    A = [-9, -6, -5, -4, -1]
    result = mss.solution_kadane(A)
    print(f"Maximum Subarray Sum Kadane: {result}")

    # Test case 3:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Maximum subarraysum bruteforce: {mss.solution_bruteforce(A)}")
    print(f"Maximum subarray sum kadane: {mss.solution_kadane(A)}")