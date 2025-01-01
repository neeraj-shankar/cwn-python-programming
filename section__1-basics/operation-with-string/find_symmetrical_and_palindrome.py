#######################################################################################################################
#     Symmetrical and Palindrome String Validation
#######################################################################################################################
""" 
Symmetrical String --> both the halves of the string are the same
example --> amaama, khokho
Palindrome --> one half of the string is the reverse of the other half or if a string appears same when read forward or
backward.
example --> amaama
"""
import re

class SymmetricalAndPalindrome:

    # Class Variable for testing purpose
    custom_string = "amaama"

    # naive approach to find whether given string is palindrome
    def test_palindrome(self):

        start_index = 0
        last_index = len(self.custom_string)-1
        mid_index = len(self.custom_string)//2
        print(f"The middle of the string --> {mid_index}")
        flag = 0

        while start_index <= mid_index:
            print(f"Star Index Status --> {start_index}")
            print(f"Last Index Status ---> {last_index}")
            if self.custom_string[start_index] == self.custom_string[last_index]:
                start_index += 1
                last_index -= 1
            else:
                flag = 1
                break
        
        if flag == 0:
            print(f"The given string is palindrome")
        else:
            print(f"The given string is not palindrome")

    # checks whether the given string is palindrome or not using slicing property
    def test_palindrome_using_slicing(self):
        matched_string = re.match("^(\w+)\Z", self.custom_string)
        print(f"The matched string -->  {matched_string}")
        if self.custom_string == self.custom_string[::-1]:
            print(f"The given string is palindrome")
        else:
            print(f"The given string is not palindrome")


""" 
Test the different methods to generate palindrome
"""
test_obj = SymmetricalAndPalindrome()

test_obj.test_palindrome()
test_obj.test_palindrome_using_slicing()

