"""
Python program to find the power of a given number using recursion approach
"""

def find_power_of_num(base, exp):
    assert int(exp) == exp, "The exponent must an integer number."
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/base * find_power_of_num(base, exp+1)
    return base * find_power_of_num(base, exp-1)


if __name__ == "__main__":
    result = find_power_of_num(2, 2.78)
    print(result)