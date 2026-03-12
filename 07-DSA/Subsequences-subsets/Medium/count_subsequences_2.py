"""
Given two string s and t. Find and return the count of all the subsquences formed in s that matches t.
"""

class SubsequenceCount():

    def solution(self, s: str, t: str)-> int:

        return self.sub(s, t, 0, 0)
    
    def sub(self, s: str, t: str, i: int, j: int)-> int:

        # Base Case: When t finishes, we found one subsequence
        if j == len(t):
            return 1
        
        # Base Case 2: When s finishes first, no valid subsequence found
        if i == len(s):
            return 0
        

        # Recursive 
        if s[i] == t[j]:

            pick = self.sub(s, t, i+1, j+1)
            skip = self.sub(s, t, i+1, j)

            return pick + skip
        
        else:

            return self.sub(s, t, i+1, j)
if __name__ == "__main__":

    sc = SubsequenceCount()

    # Test Case 1:
    s = "rabbbit"
    t = "rabbit"

    print(f"Ans: {sc.solution(s, t)}")