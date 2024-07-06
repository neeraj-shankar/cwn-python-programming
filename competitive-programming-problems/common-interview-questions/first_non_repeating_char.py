"""
Problem Statement: Find the first non-repeating character in a string.

-----------------------------------------------------------
Input: "aabbfccs"
Output: f
-----------------------------------------------------------

"""

class NonRepeatingCharacter:

    def __init__(self, input_data) -> None:

        self.input_data = input_data

    def first_non_repeating_char_dict(self):

        char_counts = {}
        for char in self.input_data:
            char_counts[char] = char_counts.get(char, 0) + 1
        
        for char in self.input_data:
            if char_counts[char] == 1:
                return char
            
        return None 
        

if __name__ == "__main__":

    raw_data = "aabbfccs"

    result = NonRepeatingCharacter(raw_data).first_non_repeating_char_dict()
    print(f"First Non Repeating Character is: {result}")
            

        