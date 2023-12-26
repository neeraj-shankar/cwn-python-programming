"""

"""


def generate_character_count(input_string):
    if not input_string:
        return ""

    result = ""
    current_char = input_string[0]
    count = 1

    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result += f"{count}{current_char}"
            current_char = char
            count = 1

    result += f"{count}{current_char}"
    return result


input_string = "aabbccabc"
output = generate_character_count(input_string)
print(output)  # Output: "2a2b2c1a1b1c"
