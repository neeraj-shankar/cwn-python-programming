"""
Given an integer array nums, sort the array based on the frequency of elements.
---------------------------------------------------------------------
Elements with lower frequency come first
If two elements have the same frequency, sort them by value (ascending)

Example Test
---------------------------------------
Input:  nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]

Example Test
---------------------------------------
Input:  [5,3,1]
Output: [1,3,5]

Example Test 3
---------------------------------------
Input:  [-1,-1,-2,-2,-2,3]
Output: [3,-1,-1,-2,-2,-2]

"""

from collections import Counter
class FrequencySort2:

    def solution(self, nums: list[int])-> list[int]:

        hm = Counter(nums)

        sorted_nums = sorted(nums, key= lambda x: (hm[x], x))

        return sorted_nums
    
if __name__ == "__main__":

    fs2 = FrequencySort2()

    nums = [1,1,2,2,2,3]
    print(f"Sorted Array: {fs2.solution(nums)}")

    nums = [5, 3, 1]
    print(f"Sorted Array: {fs2.solution(nums)}")
        