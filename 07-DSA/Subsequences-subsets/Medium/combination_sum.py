"""
Given an array of distinct integers candidates and a target integer target, return a list of all 
unique combinations of candidates where the chosen numbers sum to target. 

You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target 
is less than 150 combinations for the given input.
"""

class CombinationSum:
    total_calls = 0
    def solution(self, candidates: list[int], target: int)-> list[list[int]]:

        ans = []
        small = []
        self.combination(candidates, 0, target, 0, small, ans)
        return ans 
    
    def combination(self, candidates: list[int], start: int, target: int, curr_sum: int, small:list[int], ans: list[list[int]]):

        # Base case 1: current combination sum becomes equal to target
        if curr_sum == target:
            ans.append(small.copy())
            return
        
        if curr_sum > target:
            return

        for i in range(start, len(candidates), 1):

            small.append(candidates[i])
            curr_sum += candidates[i]

            total_calls += 1
            self.combination(candidates, i, target, curr_sum, small, ans)
            small.pop()
            curr_sum -= candidates[i]

if __name__ == "__main__":

    cs = CombinationSum()

    # Test Case 1: 
    candidates = [2,3,6,7]
    target = 7

    print(f"Combinations:\n {cs.solution(candidates, target)}")