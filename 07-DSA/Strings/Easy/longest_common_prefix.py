"""
Given the array of strings A, you need to find the longest string S, which is the prefix of ALL 
the strings in the array.

The longest common prefix for a pair of strings S1 and S2 is the longest string S 
which is the prefix of both S1 and S2.

Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".
"""

class LongestCommonPrefix():

    def solution(self, str_list: list[str]) -> str:
        """
        1. Find the smallest string len among.
        2. Take the first string as common prefix.
        3. Iterate over remaining strings in the list, any time mis-match is found at characters, update 
           it the index ending of common prefix.

        4. Finally return the result.
        """

        n = len(str_list)

        # Initialize the prefix length to the length the first string
        prefix_len = len(str_list[0])

        # Compare the prefix with each subsequent string
        for i in range(1, n):
            current_str = str_list[i]
            # find the minimum length between prefix and current string
            prefix_len = min(prefix_len, len(current_str))

            # Run inner iteration only till prefix_len, avoid redundant scanning
            for j in range(0, prefix_len):

                if current_str[j] != str_list[0][j]:
                    prefix_len = j
                    break 
        
        return str_list[0][0:prefix_len]

            



        prefix = str_list[0]
        end_idx = 0
        for i in range(1, n):
            
            for j in range(0, min_size):
                if str_list[i][j] != prefix[j]:
                    break  
                end_idx = j              

        return str_list[0][0:end_idx+1]
    
if __name__ == "__main__":

    lgp = LongestCommonPrefix()

    # Test Case 1: 
    A = ["abcdefgh", "aefghijk", "abcefgh"]
    print(f"Longest Common Prefix: {lgp.solution(A)}")

    # Test Case 2:
    A = ["abab", "ab", "abcd"];
    print(f"Longest Common Prefix: {lgp.solution(A)}")




