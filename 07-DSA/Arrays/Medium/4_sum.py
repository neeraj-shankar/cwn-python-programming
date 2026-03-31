"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

"""

class FourSum:

    def solution(self, nums: list[int], target: int):

        """
        Algo 
        -----------------------------------------
        Two loops + Two pointers

        Time and Space
        -----------------------------------------
        TC: O(n3) and SC: O(n)
        """


        n = len(nums)
        nums.sort()
        ans = []

        for i in range(0, n-3, 1):
            # Skip first duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, n-2, 1):

                # Skip second duplicate
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left, right = j+1 , n-1
                while(left < right):
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_sum == target:
                        print(f"Found a list:\n{[nums[i], nums[j], nums[left], nums[right]]}")

                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duplicates for left and right
                        while(left < right and nums[left] == nums[left+1]):
                            left += 1
                        
                        while(left < right and nums[right] == nums[right-1]):
                            right -= 1

                        left += 1
                        right -= 1

                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return ans 
    
if __name__ == "__main__":

    fs = FourSum()

    # Test case 1:
    nums = [1,0,-1,0,-2,2] 
    target = 0
    print(f"Answer: {fs.solution(nums, target)}")

    # Test case 2: Duplicates
    nums = [2,2,2,2,2]
    target = 8
    print(f"Answer: {fs.solution(nums, target)}")


