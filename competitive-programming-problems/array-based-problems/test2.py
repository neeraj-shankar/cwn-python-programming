def longest_palindrome(s):
    n = len(s)
    longest_len = 0
    start = 0
    dp = [[False] * n for _ in range(n)]
    print(f"The value in db --> {dp}")

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True
        longest_len = 1

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            longest_len = 2

    # Check for palindromes of length > 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                longest_len = length

    return s[start:start + longest_len]

"""
"""
s = "babad"
result = longest_palindrome(s)
print(result)  # Output: "bab"
