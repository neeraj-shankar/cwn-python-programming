"""
"Uniform contiguous substrings of a string" typically refers to substrings within a given string 
where all characters in the substring are the same. 

In other words, these are substrings composed of consecutive repeated characters.

For example, in the string "aaabbbbccdd", the uniform contiguous substrings are "aaa", "bbbb", "cc", and "dd". 
-----------------------------------------------------------------------------------------------------------------------

"""

def weighted_uniform_strings(s, queries):
    weights = set()
    current_char = s[0]
    current_weight = ord(current_char) - ord('a') + 1 
    weights.add(current_weight)

    for i in range(1, len(s)):
        if s[i] == current_char:
            current_weight += ord(s[i]) - ord('a') + 1
        else:
            current_char = s[i]
            current_weight = ord(s[i]) - ord('a') + 1
        weights.add(current_weight)

    result = ["Yes" if q in weights else "No" for q in queries]
    return result

# Example usage:
s = "abccddde"
queries = [1, 3, 12, 5, 9, 10]
result = weighted_uniform_strings(s, queries)
print(result)  # Output: ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'No']
