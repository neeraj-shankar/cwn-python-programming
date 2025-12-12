import re


class SuccessiveCharacterSearch:
    """
    A class to search for occurrences of a specific word in a string
    and count the characters that immediately follow each occurrence.

    Attributes:
        first_input_string (str): The predefined string to search within.
    """

    first_input_string = "geeksforgeeks is best for geeks. A geek should take interest."

    def using_loop_count_find(self):
        """
        Searches for a specific word in the predefined string and counts the characters
        that follow each occurrence.

        Steps:
        1. Identify all matches of the target word followed by any character.
        2. Extract the trailing characters of the matches.
        3. Count occurrences of each trailing character.

        Outputs:
        - A dictionary where keys are trailing characters and values are their counts.

        Complexity:
        - Time Complexity: O(n + m), where:
            * n is the length of the string.
            * m is the total number of matched substrings.
        - Space Complexity: O(m), for storing matched substrings and trailing characters.
        """

        # Target word to search
        target_word = "geek"

        # Find all occurrences of the target word followed by any character
        matched_list = re.findall(target_word + ".", self.first_input_string)
        print(f"Matched List: {matched_list}")

        # Extract the last character from each match
        trailing_characters = [match[-1] for match in matched_list]

        # Count occurrences of each trailing character
        frequency = {
            char: trailing_characters.count(char) for char in trailing_characters
        }
        print(f"Frequency of succcessive characters: {frequency}")


if __name__ == "__main__":

    SuccessiveCharacterSearch().using_loop_count_find()
