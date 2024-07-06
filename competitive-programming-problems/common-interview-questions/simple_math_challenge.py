"""
This program is determining whether a given number is prime number or not
"""
from format_output import use_case_separator
import itertools


def is_prime_number(input_number):

    """
    Takes number as input and return 1 if given number is prime else return 0
    """
    # base case scenario--> 2 is the smallest prime number
    if input_number < 2:
        return False

    if input_number in [2, 3]:
        return True

    # Condition to check if the given number is directly divisible
    # by any number from range 2 to till square root of the number
    print(f"The Square root of the given number--> {input_number**0.5}")
    for i in range(2, int(input_number**0.5) + 1):
        print(f"The division outcome of the input number-{input_number} with {i} --> {input_number / i}")
        print(f"The remainder after division of number-{input_number} with {i} -> {input_number % i}")
        if input_number % i == 0:
            return False
        else:
            return True


def math_challenge(input_number):
    """
    Takes in input number and returns if any of the permutation of given number is prime and
    returns 0 if none of the permutation is prime.
    """
    input_number_string = str(input_number)
    digit_permutation = itertools.permutations(input_number_string)

    for digits in digit_permutation:
        print(f"digit permutations --> {digits}")
        permuted_number = int(''.join(digits))
        if is_prime_number(permuted_number):
            print(f"This permuted number--> {permuted_number} turn out to be prime number")
            return 1

    return 0


"""
Function calls and input data
"""
custom_number = 910

use_case_separator()
result = math_challenge(custom_number)
print(f"The outcome all the possible combination of input number for prime number validity --> {result}")
