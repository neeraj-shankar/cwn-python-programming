"""
Problem Statement: Count the occurrences of each character in a string.

Sample Example:
-----------------------------------------------------------
Input: "aacbbeee"

Output: {
a: 2,
c: 1,
b: 2,
e: 3
}
-----------------------------------------------------------

"""

from collections import Counter


class CharacterFrequency:

    def __init__(self, input_data) -> None:
        self.input_data = input_data

    def count_characters_dictionary(self):

        char_counts = {}
        for chr in self.input_data:
            char_counts[chr] = char_counts.get(chr, 0) + 1

        return char_counts

    def count_characters_counter(self):
        return Counter(self.input_data)

    def count_characters_list(self):
        char_count = [0] * 256
        print(char_count)

        for char in self.input_data:
            char_count[ord(char)] += 1

        return char_count


if __name__ == "__main__":

    raw_data = "aabbcdrrty"

    result = CharacterFrequency(raw_data).count_characters_dictionary()
    print(f"The character frequencies: {result}")

    result = CharacterFrequency(raw_data).count_characters_counter()
    print(f"The character frequencies: {result}")

    # result = CharacterFrequency(raw_data).count_characters_list()
    # print(f"The character frequencies: {result}")
