# """
# This python program reverses the entire input string without affecting the position of special characters
# """


def reverse_string_without_changing_special_char_position(input_string):
    index = -1
    # loop from the last index to half of the string
    for i in range(len(input_string)-1, int(len(input_string)/2), -1):
        if input_string[i].isalpha():
            temp = input_string[i]
            print(f"The alphabet captured in temp --> {temp}")
            while True:
                index += 1
                if input_string[index].isalpha():
                    input_string[i] = input_string[index]
                    input_string[index] = temp
                    break

    return input_string



"""
input data and making calling to functions
"""
in_str = "abcdaefj@r#j"
string_list = list(in_str)
reversed_string = reverse_string_without_changing_special_char_position(string_list)
print("".join(reversed_string))

