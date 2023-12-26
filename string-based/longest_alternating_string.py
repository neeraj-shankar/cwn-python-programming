
"""
The Problem-solving approach
Count the frequency of each character in the string.
Iterate through all pairs of distinct characters.
For each pair, create a new string that consists of only the characters from the pair.
Find the longest valid string by removing characters that are not part of the current pair.
Return the length of the longest valid string.
"""


def alternate_characters(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    print(f"The frequency of characters in string--> {freq}")

    max_length = 0
    for char1 in freq.keys():
        for char2 in freq.keys():
            if char1 != char2:
                # input_string = "beabeefeab"
                valid_chars = [c for c in s if c == char1 or c == char2]
                print(f"The valid characters in s --> {valid_chars}")
                valid_string = ''.join(valid_chars)
                print(f"The valid string formed --> {valid_string}")
                valid = True
                for i in range(1, len(valid_string)):
                    if valid_string[i] == valid_string[i - 1]:
                        valid = False
                        break
                if valid and len(valid_string) > max_length:
                    max_length = len(valid_string)

    return max_length


# Example usage
input_string = "beabeefeab"
result = alternate_characters(input_string)
print(result)  # Output will be the length of the longest valid string
