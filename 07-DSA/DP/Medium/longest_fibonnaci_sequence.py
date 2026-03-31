"""
Given a strictly increasing array A of positive integers forming a sequence.

A sequence X1, X2, X3, ..., XN is fibonacci like if


N > =3
Xi + Xi+1 = Xi+2 for all i+2 <= N
Find and return the length of the longest Fibonacci-like subsequence of A.

If one does not exist, return 0.

NOTE: A subsequence is derived from another sequence A by deleting any number of elements 
(including none) from A, without changing the order of the remaining elements.
"""

class LongestFibonnaciSequence:

    def solution_bruteforce(self, A: list[int])-> int:
        n = len(A)

        for a in range(0, n):
            for b in range(a+1, n):
                for c in range(b+1, n):
                    if A[a] + A[b] == A[c]:
                        
    
    def solution(self, A: list[int])-> int:

        n = len(A)

        hm = {}
        for idx, num in enumerate(A):
            hm[num] = idx 
        
        dp = [[-1] * n for _ in range(n)]
        max_len = 0

        for i in range(0, n):
            for j in range(i+1, n):

                required = A[j] - A[i]

                if required in hm.keys():
                    idx = hm[required]

                    if idx < i:
                        dp[i][j] = dp[idx][i] + 1
                    else:
                        dp[i][j] = 2
                else:
                    dp[i][j] = 2

                max_len = max(dp[i][j], max_len)
        
        return max_len if max_len>=3 else 0

    
if __name__ == "__main__":

    lfs = LongestFibonnaciSequence()

    # Test Case 1: 
    A = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"Length of longest fibonnaci sequence: {lfs.solution(A)}")

    # Test Case 2: 
    A = [8,11,20,27,33,36]
    print(f"Length of longest fibonnaci sequence: {lfs.solution(A)}")
