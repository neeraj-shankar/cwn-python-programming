from collections import Counter
"""
Given a string A and a string B, find the window with minimum length in A, which will contain all the characters in B 
in linear time complexity.

Note that when the count of a character c in B is x, then the count of c in the minimum window in A should be at least x.

Note:
If there is no such window in A that covers all characters in B, return the empty string.
If there are multiple such windows, return the first occurring minimum window (with minimum start index and length)
Problem Constraints

1 <= size(A), size(B) <= 10^6

Input Format

The first argument is a string A. The second argument is a string B.

Output Format

Return a string denoting the minimum window.

Example Input

Input 1: A = "ADOBECODEBANC" B = "ABC"

Input 2: A = "Aa91b" B = "ab"

Example Output

Output 1: "BANC"
"""

class WindowSubstring:

    def solution_hm(self, A: str, B: str)-> str:
        """
        1. Create frequency map required characters
        2. Create another frequency map (have) to track currenlt available charcters and frequency.
        3.Two Variables: found and needed to track the length of found so far and required valid length.
        4. Initialize left pointer as 0. User right pointer traverse A.
        5. Add the current char at right to have map and check:
            a. Is current char in required?
            b. Is the requency of current is same in required vs have?

        6. Try and Shrink window and update valid window. By checking:
            a. Is left less and equal to right ?
            b. found is equal to needed ?
        """

        required = Counter(B)
        have = {}

        needed = len(B)
        formed = 0
        min_len = float('inf')
        left = 0
        result = ""
        for right in range(len(A)):

            char = A[right]
            have[char] = have.get(char, 0) + 1

            if char in required and have[char] == required[char]:
                formed += 1


            while left<= right and formed == needed:
                
                min_len = min(min_len, right-left+1)
                result = A[left:right+1]
                lc = A[left]
                have[lc] = have[lc] - 1

                if lc in required and have[lc] < required[lc]:
                    formed -= 1
                
                left += 1
            print(result)
        return min_len
    
if __name__ == "__main__":

    ws = WindowSubstring()

    # Test Case 1:
    A = "ADOBECODEBANC"
    B = "ABC"
    print(f"Valid Subtring: {ws.solution_hm(A, B)}")