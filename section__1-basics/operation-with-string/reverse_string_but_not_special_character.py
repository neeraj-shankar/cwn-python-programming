"""
A python program to demonstrate string reversing without changing the place of the charters
"""


def reverse_string_but_not_characters(input_string):

    # Separate the characters and store then in different lists
    letters = [char for char in input_string if char.isalpha()]
    special_characters = [c if not c.isalpha() else None for c in input_string]
    print(f"The list of letters --> {letters}")
    print(f"The list of special characters --> {special_characters}")

    # now reverse the letters
    reversed_letters = letters[::-1]
    print(f"The reversed letters --> {reversed_letters}")

    # combine the letters and string together
    reversed_string = ''.join(
        r if r is None else s for r, s in zip(reversed_letters, special_characters)
    )
    print(f"The reversed string--> {reversed_string}")



"""
input data and function calls
"""
original_string = "nee@r#j"
reverse_string_but_not_characters(original_string)

