"""
A python program to find the greatest common divsior for two given numbers. 
Common Divisor is a number that is highest number divide  both of the two given numbers without any remainder.
"""

def greatest_common_divisor(first_number, second_number):
    assert int(first_number) == first_number and int(second_number) == second_number, "The numbers must be integers only!"
    if second_number == 0:
        return first_number
    elif first_number < 0:
        first_number = -1 * first_number
    elif second_number < 0:
        second_number = -1 * second_number

    return greatest_common_divisor(second_number, first_number % second_number)

""""""
result = greatest_common_divisor(18, -6)
print(result)