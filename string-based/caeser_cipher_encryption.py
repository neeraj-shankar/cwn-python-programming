"""
-----------------------------------------------------------------------------------------------------------------------

Problem Statement:
The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to his allies. 
It works by shifting the letters in the plaintext message by a certain number of positions, known as the “shift” or “key”.

Objective:
Create a method that returns encrypted message based on raw message and shift factor given.

Example Input:
raw_message = "iamindelhi"

Example Output:
Encrypted Message: meqmrhiplm

-----------------------------------------------------------------------------------------------------------------------
"""


def caeser_encryption(input_data, shift_factor):
    encrypted_message = ""
    for char in input_data:
        if char.isalpha():
            if char.islower():
                start_ascii_number = ord("a")
            else:
                start_ascii_number = ord("A")

            new_position = (ord(char) - start_ascii_number + shift_factor) % 26
            encrypted_char = chr(start_ascii_number + new_position)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char

    return encrypted_message


if __name__ == "__main__":
    raw_message = "iamindelhi"
    shift = 4
    result = caeser_encryption(raw_message, shift)
    print(f"Encrypted Message: {result}")  # Encrypted Message: meqmrhiplm
