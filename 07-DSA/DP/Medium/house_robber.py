import sys

class HouseRobber:
    
    def solution_recursive(self, nums):
        n = len(nums)
        memo = [-1 for _ in range(n)]
        
        return self.max_sum(nums, 0, memo)
    
    def max_sum(self, nums, idx, memo):
        
        # Base Case: As soon as we all options explored
        if idx == len(nums):
            return 0
            
        skip = self.max_sum(nums, idx+1, memo)
        
        pick = self.max_sum(nums, idx+2, memo) + nums[idx]
        
        return max(skip, pick)
    
if __name__ == "__main__":
    
    hr = HouseRobber()
    sys.setrecursionlimit(1000000)
    nums = [2,7,9,3,1]
    print("Maximum Recursion Limit: ", sys.getrecursionlimit())
    print(f"Max Loot: {hr.solution_recursive(nums)}")
    print(f"Hello")