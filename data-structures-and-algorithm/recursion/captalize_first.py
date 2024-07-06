"""
Write a recursive function called capitalizeFirst. Given an array of strings, capitalize 
the first letter of each string in the array.
"""

def capitalize_first(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:]) 
    
    return result + capitalize_first(arr[1:])

answer = capitalize_first(["mango", "apple", "watermelon"])
print(answer)