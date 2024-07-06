"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix arr is shown below:

1 2 3
4 5 6
7 8 9

The left-to-right diagonal is 1 + 5 + 9 = 15 and right-to-left diagonal is 3 + 5 + 9 = 17
Their absolute difference is |15 - 17| = 2

Input format

The first line contains a single integer, n, the number of rows and columns in the square matrix .
Each of the next  lines describes a row, arr[i], and consists of  space-separated integers arr[i][j].

output format
-----------------------------------------------------------------------------------------------------------------------
Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

"""
import os


class DiagonalSumDifference(object):

    @staticmethod
    def using_naive_approach(ar):
        left_diagonal_sum = 0
        right_diagonal_sum = 0

        for i in range(0, len(ar)):
            left_diagonal_sum += ar[i][i]
            right_diagonal_sum += ar[i][len(ar)-i-1]
        print(f"The left-to-right diagonal sum --> {left_diagonal_sum}")
        print(f"The right-to-left diagonal sum -->{right_diagonal_sum}")
        abs_diff = abs(left_diagonal_sum - right_diagonal_sum)
        print(f"The absolute diagonal difference is -->{abs_diff}")
        return abs_diff


"""
"""
fptr = open('output_file.txt', 'w')
n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = DiagonalSumDifference.using_naive_approach(arr)

fptr.write(str(result) + '\n')

fptr.close()
