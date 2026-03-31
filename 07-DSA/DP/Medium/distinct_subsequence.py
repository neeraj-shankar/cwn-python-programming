"""
Given two sequences A and B, count number of unique ways in sequence A, to form a subsequence that 
is identical to the sequence B.

Subsequence : 
-----------------------------------------------------------
A subsequence of a string is a new string which is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters. 

(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
"""

class DistinctSubsequence:

    def solution_recursion(self, A: str, B: str)-> int:

        memo = [[-1] * len(B) for _ in range(len(A))]
        print(memo)
        return self.ways(A, B, 0, 0, memo)

    def ways(self, source: str, target: str, i: int, j: int, memo: list[list[int]]):

        # Base case 1: Target is exhausted, found one subsequence
        if j == len(target):
            return 1 
        
        # Base Case 2: Source is exhausted - No valid subsequence
        if i == len(source):
            return 0 
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        ans = 0
        # When Current character matches in both source and target
        if source[i] == target[j]:

            # pick call 
            pick = self.ways(source, target, i+1, j+1, memo)

            # Skip call 
            skip = self.ways(source, target, i+1, j, memo)

            ans = pick + skip
        
        # When characters don't match 
        else:
            ans = self.ways(source, target, i+1, j, memo)
        memo[i][j] = ans 

        return memo[i][j]
        
if __name__ == "__main__":

    ds = DistinctSubsequence()

    # Test Case 1:
    A = "rabbbit" 
    B = "rabbit" 
    print(f"Total Possible ways: {ds.solution_recursion(A, B)}")
