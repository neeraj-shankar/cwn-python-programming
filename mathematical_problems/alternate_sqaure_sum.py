"""
This is simple program to calculate the sum of alternate square upto given number n
pattern --> (n*n) - (n-1)(n-1) + (n-2)(n-2) - (n-3)(n-3) + (n-4)(n-4) - (n-5)(n-5) + (n-6)(n-6) - (n-7)(n-7) + ......

analysed pattern -->  adding 2n- (4+1) recursively
"""
from format_output import use_case_separator


class AlternateSquareProblem(object):

    """
    Using the naive approach of using the loop
    """

    @staticmethod
    def find_alternate_square_sum(n):

        total = 0
        for k in range(n):
            total += 2 * n - (4 * k + 1)

        print(f"The total sum of the alternate squares --> {total}")


"""
Input data and function calls
"""
num = 100

use_case_separator()
AlternateSquareProblem.find_alternate_square_sum(num)






