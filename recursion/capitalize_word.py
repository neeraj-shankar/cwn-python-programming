"""
Write a recursive function called capitalizeWords. Given an array of words, return a new array containing each word capitalized.
"""

def capitalize_word(arr):
    capitalized_arr = []
    if len(arr) == 0:
        return capitalized_arr
    
    capitalized_arr.append(arr[0].upper())
    return capitalized_arr + capitalize_word(arr[1:])

result = capitalize_word(["mango", "watermelon", "grapes"])
print(result)