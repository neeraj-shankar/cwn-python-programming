"""
Find out the number of A digit positive numbers, whose digits on being added equals to a given number B.

Note that a valid number starts from digits 1-9 except the number 0 itself. i.e. leading zeroes are not allowed.

Since the answer can be large, output answer modulo 1000000007


Problem Constraints
1 <= A <= 1000

1 <= B <= 10000

"""

class NDigitNumber:

    def solution_tda(self, A: int, B: int)-> int:

        # Edge Case 1: Maximum sum A digit number can produce is A * 9
        if B > A* 9:
            return 0
        
        memo = [[-1] * (B+1) for _ in range(A+1)]
        print(memo)

        result = 0

        for i in range(1, 10):
            if B >= (B - i):
                result = result + self.ways(A-1, B-i, memo)

    def ways(self, digits: int, rem: int, memo: list[list[int]])-> int:

        # Base Case : when there no digits left - target met 
        if  digits == 0:
            return 1 if rem == 0 else 0
        
        # Invalid Case: remaining sum falls below 0
        if rem < 0:
            return 0
        
        # Check if sub answer already computed
        if memo[digits][rem] != -1:
            return memo[digits][rem]
        print(f"Making called to ways for {digits} digits.")
        sub_result = 0
        for d in range(0, 10):
            if rem >= rem - d:
                sub_result = sub_result + self.ways(d-1, rem-d, memo)

        memo[digits][rem] = sub_result

        return memo[digits][rem]
    
if __name__ == "__main__":

    ndn = NDigitNumber()

    # Test Case 1: 
    A = 2
    B = 4
    print(f"Total Numbers count: {ndn.solution_tda(A, B)}")