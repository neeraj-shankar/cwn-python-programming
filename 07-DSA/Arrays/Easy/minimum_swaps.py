"""
Given an array of integers A and an integer B, find and return the minimum number of swaps 
required to bring all the numbers less than or equal to B together.

Note: It is possible to swap any two elements, not necessarily consecutive.
"""

class MininumSwaps():

    def solution_bruteforce(self, nums: list, target: int)-> int:
        """
        """
        pass 

    def solution_sliding_window(self, nums: list, target: int)-> int:
        """
        1. Count the number of elements less than equal to target.
        3. Create first window of size the count above.
        4. Maintain the count of bad elements (greater than target) for each window
        """

        n = len(nums)

        # Base Case: There is no swap needed for array size less than 3
        if n <= 2:
            return 0 
        # Count number of elements less than equal to target
        k = 0
        for i in range(0, n):

            if nums[i] <= target:
                k += 1
        
        # Create window of size k and maintain count of bad elements
        bad_count = 0
        for j in range(0, k):
            if nums[j] > target:
                bad_count += 1
        
        # Traverse through remaining window and maintain min bad count
        ans = bad_count
        for end in range(k, n):
            st = end - k
            # If incoming element is smaller or equal of target and falling out element greater
            # than the target, decrease bad count
            # if nums[st] > target and nums[end] <= target:
            #     bad_count -= 1

            # elif nums[st] <= target and nums[end] > target:
            #     bad_count += 1

            if nums[end] > target:
                bad_count += 1
            
            if nums[st] > target:
                bad_count -= 1

            ans = min(ans, bad_count)
            st += 1


        return ans
if __name__ == "__main__":

    ms = MininumSwaps()

    # Test case 1:
    A = [1, 12, 10, 3, 14, 10, 5]
    B = 8
    print(f"Minimum number of swaps required: {ms.solution_sliding_window(A, B)}")

    # Test case 2:
    A = [5, 17, 100, 11]
    B = 20
    print(f"Minimum number of swaps required: {ms.solution_sliding_window(A, B)}")

    # Test Case 3: 
    A = [52,7,93,47,68,26,51,44,5,41,88,19,78,38,17,13,24,74,92,5,84,27,48,49,37,59,3,56,79,26,55,60,16,83,63,40,55,9,96,29,7,22,27,74,78,38,11,65,29,52,36,21,94,46,52,47,87,33,87,70]
    B = 19
    print(f"Minimum number of swaps required: {ms.solution_sliding_window(A, B)}")

