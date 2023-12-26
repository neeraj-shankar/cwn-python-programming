"""
Write a recursive function called isPalindrome which returns true if the string passed to 
it is a palindrome (reads the same forward and backward). Otherwise it returns false.
"""

def is_palidrome(my_string):
    if len(my_string) == 0:
        return True
    if my_string[0] != my_string[len(my_string)-1]:
        return False
    
    return is_palidrome(my_string[1:-1])

result = is_palidrome("abcba")
print(result)