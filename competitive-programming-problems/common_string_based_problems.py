import re

class AlternateStringProblem:
    """
    A class to solve the problem of common problems which are based on the strings in python programming.

    Methods
    -------
    min_deletion_required_greedy(input_string):
        Uses a greedy approach to count the minimum number of deletions required.

    min_deletion_required_linear_scan(raw_data):
        Uses a frequency count to determine the number of deletions required to
        achieve an alternating string.

    Example
    -------
    >>> input_string = "AAABBB"
    >>> print(AlternateStringProblem.first_approach(input_string))
    Final String: ['A', 'B']
    4

    >>> raw_data = "AAABBB"
    >>> print(AlternateStringProblem.second_approach(raw_data))
    4
    """

    @staticmethod
    def min_deletion_required_greedy(input_string):
        """
        Uses a greedy approach to count the minimum number of deletions required
        to make the string alternate between different characters.

        Parameters
        ----------
        input_string : str
            The input string to process.

        Returns
        -------
        int
            The minimum number of deletions required.

        Time Complexity
        ---------------
        O(n): Where n is the length of the input string. Each character is processed once.

        Space Complexity
        ----------------
        O(n): Space is used for the final_string list, which can grow to the size of the input string.

        Example
        -------
        >>> input_string = "AAABBB"
        >>> print(AlternateStringProblem.first_approach(input_string))
        Final String: ['A', 'B']
        4
        """
        number_of_deletion = 0
        final_string = []  # This list will store the result after removing duplicates
        key = input_string[0]  # This will be used for comparison
        final_string.append(key)
        for char in input_string[1:]:
            # If the current character is the same as the base character, it's a duplicate (matching adjacent character)
            # It needs to be removed, so the deletion count increases
            if key == char:
                number_of_deletion += 1
            else:
                # Otherwise, update the base character with the current character
                key = char
                final_string.append(char)
        print(f"Final String: {final_string}")
        return number_of_deletion

    @staticmethod
    def min_deletion_required_linear_scan(raw_data):
        """
        Uses a linear scan to determine the number of deletions required to
        achieve an alternating string by comparing adjacent characters.

        Parameters
        ----------
        raw_data : str
            The input string to process.

        Returns
        -------
        int
            The minimum number of deletions required.

        Time Complexity
        ---------------
        O(n): Where n is the length of the input string. Each character is processed once.

        Space Complexity
        ----------------
        O(1): Uses a constant amount of extra space.

        Example
        -------
        >>> raw_data = "AAABBB"
        >>> print(AlternateStringProblem.second_approach(raw_data))
        4
        """
        number_of_deletion = 0
        for i in range(1, len(raw_data)):
            # If the current character is the same as the previous character, it's a duplicate (matching adjacent character)
            # It needs to be removed, so the deletion count increases
            if raw_data[i] == raw_data[i - 1]:
                number_of_deletion += 1
        return number_of_deletion

    def caeser_encryption(input_data, shift_factor):
        """
        Encrypts the input string using Caesar cipher encryption.

        Parameters
        ----------
        input_data : str
            The input string to be encrypted.
        shift_factor : int
            The number of positions to shift each character.

        Returns
        -------
        str
            The encrypted string.

        Example
        -------
        >>> input_data = "Hello, World!"
        >>> shift_factor = 3
        >>> print(caeser_encryption(input_data, shift_factor))
        'Khoor, Zruog!'

        Time Complexity
        ---------------
        O(n): Where n is the length of the input string. Each character is processed once.

        Space Complexity
        ----------------
        O(n): The space required for the output string, which is proportional to the length of the input string.
        """

        encrypted_message = ""  # Initialize the resulting encrypted message

        for char in input_data:
            if char.isalpha():  # Check if the character is an alphabet letter
                # Determine the ASCII start number based on case
                start_ascii_number = ord("a") if char.islower() else ord("A")

                # Calculate new position after shifting by shift_factor
                new_position = (ord(char) - start_ascii_number + shift_factor) % 26

                # Convert the new position back to a character
                encrypted_char = chr(start_ascii_number + new_position)

                # Append the encrypted character to the result
                encrypted_message += encrypted_char
            else:
                # Non-alphabet characters are added directly without encryption
                encrypted_message += char

        return encrypted_message  # Return the fully encrypted message

    def caeser_encryption_generator(input_data, shift_factor):
        """
        This method uses a generator function to produce each character of the encrypted string one at a time, 
        which can be useful for handling large strings or streaming data.

        Parameters
        ----------
        input_data : str
            The input string to be encrypted.
        shift_factor : int
            The number of positions to shift each character.

        Returns
        -------
        str
            The encrypted string.

        Example
        -------
        >>> input_data = "Hello, World!"
        >>> shift_factor = 3
        >>> print(caeser_encryption_generator(input_data, shift_factor))
        'Khoor, Zruog!'

        Time Complexity
        ---------------
        O(n): Where n is the length of the input string. Each character is processed once.

        Space Complexity
        ----------------
        O(n): The space required for the output string, which is proportional to the length of the input string.
        """

        def shift_char(char, shift_factor):
            if char.isalpha():
                start_ascii_number = ord("a") if char.islower() else ord("A")
                return chr(
                    (ord(char) - start_ascii_number + shift_factor) % 26
                    + start_ascii_number
                )
            return char

        return "".join(shift_char(char, shift_factor) for char in input_data)

    def funny_string_list_comprehension(self, input_string):
        """
        Determine if the input string is funny using list comprehension implementation.

        A string is considered funny if the absolute differences in the ASCII values of
        its characters, when compared to its reversed string, are the same.

        Returns:
            str: "Funny" if the string is funny, "Not Funny" otherwise.

        Example:
            >>> obj = FunnyStringCompilation("bcxz")
            >>> obj.funny_string_list_comprehension()
            'Not Funny'

        Time Complexity:
            O(n): Where n is the length of the input string.

        Space Complexity:
            O(n): Due to the storage of absolute differences in lists.
        """
        # Reverse the input string
        reversed_string = self.input_string[::-1]

        # Calculate the absolute differences in ASCII values for the original string
        abs_difference_original = [
            abs(ord(input_string[i]) - ord(input_string[i - 1]))
            for i in range(1, len(input_string))
        ]

        # Calculate the absolute differences in ASCII values for the original string
        abs_difference_reversed = [
            abs(ord(reversed_string[i]) - ord(reversed_string[i - 1]))
            for i in range(1, len(reversed_string))
        ]

        # Compare the lists of absolute differences
        if abs_difference_original == abs_difference_reversed:
            return "FUNNY"
        else:
            return "NOT FUNNY"

    def super_reduced_string(s: str) -> str:
        """
        Reduce the input string by removing pairs of adjacent matching characters.
        If the resulting string is empty, return "Empty String".

        Args:
            s (str): The input string to process.

        Returns:
            str: The reduced string or "Empty String" if the reduced string is empty.

        Example:
            >>> super_reduced_string("aaabccddd")
            'abd'
            >>> super_reduced_string("aa")
            'Empty String'

        Time Complexity:
            O(n): The function processes each character in the input string once.

        Space Complexity:
            O(n): The function uses a stack to store characters, which in the worst case can be as large as the input string.

        """
        char_stack = []

        for char in s:
            # Check if char_stack is not empty and the top value matches the current char
            # If matched, pop that character (remove the pair)
            if char_stack and char_stack[-1] == char:
                char_stack.pop()
            # Else, add the current char to the stack
            else:
                char_stack.append(char)

        # Fetch each char from char_stack and join them as a single string
        reduced_string = "".join(char_stack)

        # Return reduced_string if it is not empty, else return "Empty String"
        return reduced_string if reduced_string else "Empty String"

    def reverse_string_index_based(input_string: list, left: int, right: int) -> None:
        """
        Reverse the elements of the input list between the indices left and right (inclusive).

        Args:
            input_string (list): The list of characters to be reversed.
            left (int): The starting index of the section to be reversed.
            right (int): The ending index of the section to be reversed.

        Returns:
            None: This function modifies the input list in place and does not return a value.

        Example:
            >>> input_string = ['a', 'b', 'c', 'd', 'e']
            >>> rev(input_string, 1, 3)
            >>> input_string
            ['a', 'd', 'c', 'b', 'e']

        Time Complexity:
            O(n): Where n is the number of elements between left and right indices.
            Each element in this range is swapped once.

        Space Complexity:
            O(1): The function uses a constant amount of extra space.
        """
        # Loop until the left index is less than the right index
        while left < right:
            # Swap the elements at the left and right indices
            temp = input_string[left]
            input_string[left] = input_string[right]
            input_string[right] = temp
            # Move the left index one step to the right
            left += 1
            # Move the right index one step to the left
            right -= 1

    def generate_character_count(input_string: str) -> str:
        """
        Generate a character count string where each character is followed by the number of times it appears consecutively in the input string.

        Args:
            input_string (str): The input string to process.

        Returns:
            str: A string representing the character count where each character is followed by the number of times it appears consecutively.

        Example:
            >>> generate_character_count("aaabbc")
            '3a2b1c'
            >>> generate_character_count("aabccc")
            '2a1b3c'

        Time Complexity:
            O(n): Where n is the length of the input string. The function processes each character once.

        Space Complexity:
            O(n): The resulting string can be as long as twice the input string in the worst case (when all characters are unique).

        """
        # Check if the input string is empty
        if not input_string:
            return ""

        result = ""
        current_char = input_string[0]  # Initialize the current character
        count = 1  # Initialize the count of the current character

        # Iterate through the string starting from the second character
        for char in input_string[1:]:
            if char == current_char:
                # If the current character is the same as the previous one, increment the count
                count += 1
            else:
                # Append the count and the current character to the result
                result += f"{count}{current_char}"
                # Update the current character and reset the count
                current_char = char
                count = 1

        # Append the count and the last character to the result
        result += f"{count}{current_char}"
        return result

    def word_count_using_regex(sentence):
        """
        Calculate the number of words in a sentence using a regular expression.

        This function uses a regular expression to find words in a given sentence.
        A word is defined as a sequence of characters starting with an uppercase letter
        followed by zero or more lowercase letters. The function prints the list of words
        found and the total word count.

        Parameters:
        sentence (str): The input sentence to be evaluated.

        Returns:
        int: The total number of words in the sentence.

        Time Complexity: O(n), where n is the length of the input sentence.
        Space Complexity: O(w), where w is the number of words found in the sentence.

        Example Usage:
        >>> sentence = "Hello World This Is A Test"
        >>> word_count_using_regex(sentence)
        ['Hello', 'World', 'This', 'Is', 'A', 'Test']
        Word Count: 6
        """

        # Initialize the total word count
        total_words = 1

        # Define the regular expression to match words starting with an uppercase letter
        re_expression = r"[A-Z][a-z]*"

        # Find all words in the sentence that match the regular expression
        words = re.findall(re_expression, sentence)

        # Calculate the total number of words
        total_words = len(words)

        # Print the list of words found
        print(words)

        # Print the total word count
        print(f"Word Count: {total_words}")

        # Return the total word count
        return total_words


    def validate_strong_password(n, password):
        """
        Validate the strength of a password based on specific criteria.

        This method checks if a password meets the following criteria:
        1. Its length is at least 6 characters.
        2. It contains at least one digit.
        3. It contains at least one lowercase English character.
        4. It contains at least one uppercase English character.
        5. It contains at least one special character.

        Parameters:
        n (int): The length of the password.
        password (str): The password to be validated.

        Returns:
        int: The number of additional characters needed to make the password strong.

        Time Complexity: O(n), where n is the length of the password.
        Space Complexity: O(1), as the space used does not depend on the input size.

        Example Usage:
        >>> PasswordValidator.validate_strong_password(5, "Ab1!")
        2
        """

        # Initialize the count of different character types
        character_count = {
            "special_char": 0,
            "digit_char": 0,
            "capital_char": 0,
            "small_char": 0,
        }

        # Calculate the number of characters needed to reach the minimum length of 6
        required_char_count = max(0, 6 - n)
        missing_char_count = 0

        # Iterate through each character in the password
        for char in password:
            print(f"The char in iteration --> {char}")
            if char.isdigit():
                character_count["digit_char"] += 1
            elif char.isupper():
                character_count["capital_char"] += 1
            elif char.islower():
                character_count["small_char"] += 1
            elif not char.isalnum():
                character_count["special_char"] += 1

        # Count the number of missing character types
        for val in character_count.values():
            if val == 0:
                print(f"the item value --> {val}")
                print(f"Missing char count  --> {missing_char_count}")
                missing_char_count += 1

        print(f"the required count --> {required_char_count}")
        print(f"The missing char count --> {missing_char_count}")
        print(f"the dictionary data--> {character_count}")

        # Return the maximum of required characters to reach length 6 or missing character types
        return max(required_char_count, missing_char_count)



if __name__ == "__main__":
    input_string = "AAABBB"
    print(AlternateStringProblem.first_approach(input_string))

    raw_data = "AAABBB"
    print(AlternateStringProblem.second_approach(raw_data))
