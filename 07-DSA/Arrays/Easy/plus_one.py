"""
You are given a large integer represented as an integer array digits, where each digits[i] is 
the ith digit of the integer. The digits are ordered from most significant 
to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class PlusOne:

    def solution_bruteforce(self, digits: list[int])-> list[int]:

        n = len(digits)

        if digits[n-1] < 9:
            digits[n-1] = digits[n-1] + 1

            return digits
        
        carry = 1

        for i in range(n, -1, -1):

            num = digits[i] + carry

            digits[i] = num % 10

            carry = num // 10

            if carry == 0:
                return digits
        
        return [1] + digits
    
    def solution_optimal(self, digits: list[int])-> list[int]:

        n = len(digits)

        for i in range(n-1, -1, -1):

            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0

        return [1] + digits
