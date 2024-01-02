"""
Here's a simple mapping of ASCII values for commonly used characters:
-----------------------------------------------------------------------------------------
Lowercase letters (a-z): 97-122
Uppercase letters (A-Z): 65-90
Digits (0-9): 48-57
Special characters:

    Space: 32
    !: 33
    ": 34
    #: 35
    $: 36
    %: 37
    &: 38
    ': 39
    (: 40
    ): 41
    *: 42
    +: 43
    ,: 44
    -: 45
    .: 46
    /: 47
"""

# Getting the Ascii Value of a string
ascii_value_of_A = ord("A")
print(f"Ascii Value of A: {ascii_value_of_A}")

# Util method to provide ascii value
def get_ascii_value(char):
    """
    ascii_value takes in char as argument and returns its ascii value.

    Args: Takes char as the argument

    Returns: The Ascii Value of the given character
    """
    ascii_value = ord(char)
    return ascii_value

# Getting String from provided ascii value
given_ascii_value = 65
corresponding_char = chr(given_ascii_value)
print(f"Char at 65 in Ascii Table: {corresponding_char}")