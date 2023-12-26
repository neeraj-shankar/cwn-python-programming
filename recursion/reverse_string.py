"""
Write a recursive function called reverse which accepts a string and returns a new string in reverse.
"""

def reverse_string(input_string):
    if len(input_string) <= 1:
        return input_string
    print(input_string[0:len(input_string)-1])
    return input_string[len(input_string)-1] + reverse_string(input_string[0:len(input_string)-1])

result = reverse_string("python")
print(result)