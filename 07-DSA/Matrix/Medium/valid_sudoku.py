"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according
to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

"""


class ValidSudoku:

    def solution_bruteforce(self, board: list[list[chr]]) -> bool:
        """
        Algorithm
        ---------------------------------------------------
        The algorithm runs in constant time O(1) and constant space O(1) since the Sudoku board size 
        is fixed at 9×9. Conceptually, for an N×N board, the time complexity would be O(N²) with O(N²) 
        auxiliary space. The solution is already optimal; 
        
        further optimizations would only reduce constant factors, such as using bitmasks instead of sets.
        """

        n = len(board)
        m  = len(board[0])

        # Create list of sets for lookup
        rows = [set() for _ in range(n)]
        columns = [set() for _ in range(m)]
        boxes = [set() for _ in range(n)]

        for i in range(n):

            for j in range(m):
                val = board[i][j]
                if '1' <= val <= '9':
                    # Check current cell in rows
                    if val in rows[i]:
                        print(f"Duplicate in Row: {i}, Check the set: {rows[i]}")
                        return False
                    
                    # Similarly, validate colums data
                    if val in columns[j]:
                        return False
                    
                    # Boxes calculation and validation
                    boxRow = (i//3) 
                    boxCol = (j//3)

                    box_index = (boxRow * 3) + boxCol
                    if val in boxes[box_index]:
                        print("Matched me box")
                        return False

                    # Numbers to the respective row, col and boxes
                    rows[i].add(val)
                    columns[j].add(val)
                    boxes[box_index].add(val)
        return True


if __name__ == "__main__":

    vs = ValidSudoku()

    # Test Case 1:
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    print(f"Is the given sudoku valid: {vs.solution_bruteforce(board)}")

    # Test Case 2:
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(f"Is the given sudoku valid: {vs.solution_bruteforce(board)}")

