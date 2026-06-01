"""
Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index).
"""

class LongestPalindromicSubstring:

    def solution_bruteforce(self, A:str)-> str:
        pass 

    def solution(self, A: str)-> str:
        n = len(A)

        max_len = float('-inf')

        # Even length substring 
        for i in range(0, n, 1):
            left, right = i, i+1

            while (left >= 0 and right < n):

                if A[left] != A[right]:
                    break

                left -= 1
                right += 1
            max_len = max(max_len, right-left-1)

        
        # Odd length substring
        for i in range(0, n, 1):
            left, right = i-1, i+1

            while (left >= 0 and right < n):

                if A[left] != A[right]:
                    break

                left -= 1
                right += 1
            max_len = max(max_len, right-left-1)

        return max_len


if __name__ == "__main__":

    lps = LongestPalindromicSubstring()

    # Test case 1:
    A = "a"
    print(f"Longest Palindromic Substring: {lps.solution(A)}")
