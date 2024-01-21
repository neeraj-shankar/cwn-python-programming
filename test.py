raw_message = "iamindelhi"
shift_factor = 4
encrypted_message = ""

for char in raw_message:
    if char.isalpha():
        if char.isupper():
            starting_ascii_number = ord('A')
        else:
            starting_ascii_number = ord('a')
        shift_pos = (ord(char) - starting_ascii_number + shift_factor) % 26
        new_char = chr(starting_ascii_number + shift_pos)
        encrypted_message += new_char
print(encrypted_message)
        
