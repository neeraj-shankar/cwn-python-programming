"""
Return only unique elements sorted by frequency (not repeated)

Example Test
---------------------------------------
Input:  [1,1,2,2,2,3]
Output: [3,1,2]
"""

class FrequencySort:

    def solution(self, nums: list[int])-> int:
        n = len(nums)

        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        print(hm)

        sorted_nums = sorted(hm.items(), key= lambda x: (x[1], x[0]))
        print(sorted_nums)

        return [x[0] for x in sorted_nums]

if __name__ == "__main__":

    fs = FrequencySort()

    nums = [2, 2, 3, 3, 3, 1, 1, 1, 1, 4]
    print(f"Sorted Array based on frequency: {fs.solution(nums)}")