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
        This method uses a generator function to produce each character of the encrypted string one at a time, which can be useful for handling large strings or streaming data.

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


if __name__ == "__main__":
    input_string = "AAABBB"
    print(AlternateStringProblem.first_approach(input_string))

    raw_data = "AAABBB"
    print(AlternateStringProblem.second_approach(raw_data))
