"""
Find out the number of A digit positive numbers, whose digits on being added equals to a given number B.

Note that a valid number starts from digits 1-9 except the number 0 itself. 
i.e. leading zeroes are not allowed. Since the answer can be large, output answer modulo 1000000007
"""


class NDigitsNumbers():

    def solution_tda(self, A, B):

        # Create DP array to store already calculated ans.
        dp = [[-1] * (B+1) for _ in range(A+1)]

        # Fill Base cases:

        # Base Case 1: There are 0 numbers of 1 digit whose sum is 0 (0 not allowed)
        dp[1][0] = 0

        # # Base Case 2: There are always 1 number of 1 digit whose sum is less than or equal to 9
        # for i in range(1, 10):
        #     dp[1][i] = 1

        # # Base case 2: There cannot be 1 digit number whose sum is greater than 9
        # for i in range(10, B+1):
        #     dp[1][i] = 0
        
        print(dp)



if __name__ == "__main__":

    ndn = NDigitsNumbers()

    A = 2
    B = 4

    print(ndn.solution_tda(A, B))

