"""
Python program to find sum digits of a given positive integer
"""

def sum_of_digits(input_number):
    assert input_number >=0 and int(input_number) == input_number, 'The input number cannot be negative or non-integer'
    if input_number == 0:
        return 0
    else:
        return (input_number%10) + sum_of_digits((input_number//10))


# calling the function
result = sum_of_digits(22.30)
print(result)