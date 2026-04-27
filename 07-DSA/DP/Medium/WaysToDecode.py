"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message denoted by string A containing digits, determine the total number of 
ways to decode it modulo 109 + 7.
-----------------------------------------------------------------------------------------


Problem Constraints
-----------------------------------------------------------------------------------------
1 <= length(A) <= 105

Input Format
-----------------------------
The first and the only argument is a string A.

Output Format
-----------------------------
Return an integer, representing the number of ways to decode the string modulo 109 + 7.

Example Input
-----------------------------------------------------------------------------------------
Input 1: A = "12"
Input 2: A = "8"

Example Output
-------------------------------------------------
Output 1: 2
Output 2: 1

Example Explanation
-------------------------------------------------
Explanation 1:
 Given encoded message "12", it could be decoded as "AB" (1, 2) or "L" (12).
 The number of ways decoding "12" is 2.
-------------------------------------------------
"""

class WaysToDecode:
    calls = 0
    def solve_tda(self, A: str):
        memo = [-1] * len(A)

        return self.ways(A, 0, memo)
    
    def ways(self, s: str, idx: int, memo: list[int])-> int:
        """
        
        """

        if idx == len(s):
            return 1
        
        if memo[idx] != -1:
            return memo[idx]
        self.calls += 1
        print(f"Making {self.calls}th call....")

        # Select single number 
        select_one = self.ways(s, idx+1, memo)

        # Select the combination of two
        select_two = 0
        if idx < len(s) - 1 and int(s[idx] + s[idx+1]) <= 26:
            select_two = self.ways(s, idx+2, memo)

        memo[idx] = select_one + select_two
        return memo[idx]

if __name__ == "__main__":

    wtd = WaysToDecode()

    # Test Case 1:
    A = "12"
    print(f"Total Number of ways: {wtd.solve_tda(A)}")

    wtd.calls = 0
    # Test Case 2:
    A = '1268'
    print(f"Total Number of ways: {wtd.solve_tda(A)}")


