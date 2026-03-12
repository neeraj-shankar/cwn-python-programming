"""
Given an unsorted integer array, A of size N. Find the first missing positive integer.
Note: Your algorithm should run in O(n) time and use constant space.
"""

class FirstMissingInteger():

    def solution_sorting(self, nums: list) -> int:
        """
        1. Sort the array in ascending order of value.
        2. Traverse the array neglect negative numbers.
        3. Starting from first positive number, compare if difference between current and previous element 
           is greater than 1, return current - 1
        """
        pass

    def solution_optimal(self, nums: list) -> int:
        """
        1. Replace all the negative numbers with size of array + 2 ( impossible answers)
        2. Mark the correct position of the ith element in a sorted array. That is, current 
           element in array, mark current - 1 as its correct position in a sorted array.
        3. Once marked, traverse the array, return index + 1 for the first positive number found.

        Time and Space Complexity
        ---------------------------------------------------
        TC: O(N) --> Three passes N + N + N
        SC: O(1)
        """

        n = len(nums)

        # Mark negative and 0 number with n+2 --> they do not contribute to answer
        for idx, num in enumerate(nums):
            if num <= 0:
                nums[idx] = n + 2

        
        # Mark the correct position of current number in an sorted array
        for idx in range(0, n):

            num = abs(nums[idx])
            pos = num - 1

            # Mark the number this idx as negative
            if num < n+1:
                nums[pos] = -1 * abs(nums[pos])
        
        # print(f"Final State of nums: {nums}")    
        # Return idx + 1 first positive number encountered
        for idx , num in enumerate(nums):
            if num > 0:
                return idx + 1
            
        # All indices are marked so n+1 is missing
        return n + 1
    
if __name__ == "__main__":

    fmi = FirstMissingInteger()

    # Test case 1: Positive integers with 0
    A = [1, 2, 0]
    print(f"First missing positive integer: {fmi.solution_optimal(A)}")

    # Test Case 2: Negative positive mixed
    A = [3, 4, -1, 1]
    print(f"First missing positive integer: {fmi.solution_optimal(A)}")

    # Test Case 3: All Negative Integers
    A = [-8, -7, -6]
    print(f"First missing positive integer: {fmi.solution_optimal(A)}")

    # Test Case 4: N + 1 missing 
    A = [1, 2, 3, 4]
    print(f"First missing positive integer: {fmi.solution_optimal(A)}")






