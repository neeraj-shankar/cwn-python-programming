class ComplexStringQuestions:

    def __init__(self) -> None:
        pass

    def alternate_characters(s):
        """
        Calculate the length of the longest valid string that can be created by alternating two distinct characters.

        This function iterates through all pairs of distinct characters in the input string `s` and finds the longest
        valid string that can be formed by alternating these two characters. A valid string is one where no two adjacent
        characters are the same.

        Parameters:
        s (str): The input string to be evaluated.

        Returns:
        int: The length of the longest valid string that can be formed by alternating two distinct characters.

        Time Complexity: O(n^2 * m), where n is the number of unique characters in the string and m is the length of the string.
        Space Complexity: O(m), where m is the length of the string.

        Example Usage:
        >>> s = "beabeefeab"
        >>> alternate_characters(s)
        5
        """

        # Calculate the frequency of each character in the string
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        print(f"The frequency of characters in string --> {freq}")

        max_length = 0

        # Iterate through all pairs of distinct characters
        unique_chars = list(freq.keys())
        for i in range(len(unique_chars)):
            for j in range(i + 1, len(unique_chars)):
                char1 = unique_chars[i]
                char2 = unique_chars[j]

                # Filter the string to include only the two characters
                valid_chars = [c for c in s if c == char1 or c == char2]
                print(f"The valid characters in s --> {valid_chars}")

                # Check if the filtered string is valid (no two adjacent characters are the same)
                valid = True
                for k in range(1, len(valid_chars)):
                    if valid_chars[k] == valid_chars[k - 1]:
                        valid = False
                        break

                # Update the maximum length if the valid string is longer
                if valid:
                    max_length = max(max_length, len(valid_chars))

        return max_length
    
    def is_beautiful(self, s):
        """
        Determine if a string is beautiful by checking if it can be split into a sequence
        of two or more positive integers where each integer is exactly one more than the previous integer.

        Parameters:
        s (str): The input string to be evaluated.

        Returns:
        str: "YES" if the string is beautiful, otherwise "NO".

        Time Complexity: O(n^2), where n is the length of the input string.
        Space Complexity: O(n), where n is the length of the input string.

        Example Usage:
        >>> s = "91011"
        >>> is_beautiful(s)
        'YES'
        """

        n = len(s)
        
        # Iterate through possible lengths of the first number in the sequence
        for i in range(1, n // 2 + 1):
            first_num = s[:i]
            print(f"First Number --> {first_num}")
            
            # Skip if the first number has a leading zero
            if first_num.startswith('0'):
                continue

            # Initialize the sequence with the first number
            seq = [int(first_num)]
            print(f"Initialized sequence: {seq}")
            j = i
            
            # Build the sequence by appending the next expected number
            while j < n:
                next_num = seq[-1] + 1
                print(f"Next Num: {next_num}")
                next_num_str = str(next_num)
                
                # Check if the next expected number is a substring starting at position j
                if s.startswith(next_num_str, j):
                    seq.append(next_num)
                    j += len(next_num_str)
                else:
                    # If we can't continue the sequence, break the loop
                    break

            # Check if the entire string has been used and the sequence has at least two numbers
            if j == n and len(seq) >= 2:
                return "YES"

        return "NO"

# Example usage
if __name__ == "__main__":

    complexStringQuestions = ComplexStringQuestions()
    s = "beabeefeab"
   # print(complexStringQuestions.alternate_characters(s))  # Outputs: 5

    input_string = "91011"

    result = complexStringQuestions.is_beautiful(input_string)
    print(f"Outcome: {result}")
