"""
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order 
and return the generated square matrix.

Input: 5

Output:
[ [1,   2,  3,  4, 5], 
  [16, 17, 18, 19, 6], 
  [15, 24, 25, 20, 7], 
  [14, 23, 22, 21, 8], 
  [13, 12, 11, 10, 9] ]

"""

class SpiralOrderMatrix():

    def solution_bruteforce(self, A):
        pass 

    def solution_optimized(self, A: int)-> list[list[int]]:

        # Create matrix of size A * A store answer
        matrix = [[0]*A for _ in range(A)]

        row = 0
        col = 0
        val = 1

        while A > 1:
            # Fill the top row from left --> col increases
            for k in range(0, A-1):
                matrix[row][col] = val
                val += 1
                col += 1

            # Fill the right column from top --> row increases
            for k in range(1, A):
                matrix[row][col] = val 
                val += 1
                row += 1

            # Fill the bottom row from right --> col decreases
            for k in range(1, A):
                matrix[row][col] = val 
                val += 1
                col -= 1

            # Fill the bottom right column from bottom --> row decreases
            for k in range(1, A):
                matrix[row][col] = val 
                val += 1
                row -= 1

            # Move row one step ahead and move col one step ahead
            row += 1
            col += 1
            A = A - 2

        # Handle the odd case 
        if A == 1:
            matrix[row][col] = val 

        return matrix
if __name__ == "__main__":

    som = SpiralOrderMatrix()

    # Test Case 1: 
    A = 80
    print(f"Spiral Order Matrix Optimized: {som.solution_optimized(A)}")
