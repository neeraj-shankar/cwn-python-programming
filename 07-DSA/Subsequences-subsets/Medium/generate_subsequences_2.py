"""
Given an array, generate all the unique subsequences. 

Note: Array may contain duplicates
"""


class GenerateSubsequence:

    def solve(self, nums: list[int])-> list[list[int]]:

        ans = [] # List to store all the unique subsequences
        small = [] # one subsequence

        self.sub(nums, 0, small, ans)
        return ans
    

    def sub(self, nums: list[int], start: int, small: list[int], ans: list[list[int]])-> None:

        # Base Case: add the generate subsequence to the answer
        print(small)
        ans.append(small.copy())

        for i in range(start, len(nums), 1):

            # Add the check to skip duplicates
            if i > start and nums[i] == nums[i-1]:
                continue

            # Add the current element to subsequence
            small.append(nums[i])

            # Make recursive call to sub
            self.sub(nums, i+1, small, ans)

            # While going back, undo the changes
            small.pop()

if __name__ == "__main__":

    gs = GenerateSubsequence()

    # Test case 1:
    nums = [1,2,2]
    print(gs.solve(nums))