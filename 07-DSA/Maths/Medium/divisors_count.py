"""
Given an array of integers A, find and return the count of divisors of each element of the array.
NOTE: The order of the resultant array should be the same as the input array.
"""
import math
class Divisors:

    def count_divisors(self, A: list[int])-> list[int]:
        
        n = len(A)

        # get the max of the array elements
        maxi = float('-inf')
        for num in A:
            maxi = max(maxi, num)

        spf = self._get_spf(maxi)
        counts = [0] * n
        for i in range(0, n, 1):
            num = A[i]
            ans = 1
            while(num > 1):
                s = spf[num]
                count = 0
                while (num % s == 0):
                    num = num // s 
                    count += 1
                ans = ans * (count+1)
            
            counts[i] = ans 
        print(counts)

    
    def _get_spf(self, N: int)-> list[int]:

        # Cretae a list to store smallest prime factor of numbers from 1 to N
        spf = [0]* (N+1)
        n = len(spf)
        # Assume every number is the smallest prime factor of itself
        for i in range(len(spf)):
            spf[i] = i 
        
        print(spf)
        for i in range(2, int(n**0.5)+1, 1):

            if spf[i] == i:
                for j in range(i*i, len(spf), i):
                    if spf[j] == j:
                        spf[j] = i
        
        return spf


if __name__ == "__main__":
    A = [2, 3, 4, 5]
    Divisors().count_divisors(A)