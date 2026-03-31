"""
Given 2 integers A and B and an array of integers C of size N. Element C[i] represents the length of ith board.
You have to paint all N boards [C0, C1, C2, C3 … CN-1]. 

There are A painters available and each of them takes B units of time to paint 1 unit of the board.

Calculate and return the minimum time required to paint all boards under the constraints 
that any painter will only paint contiguous sections of the board.

NOTE:
1. 2 painters cannot share a board to paint. 
--------------------------------------------------
That is to say, a board cannot be painted partially by one painter, and partially by another.

2. A painter will only paint contiguous boards. 
-----------------------------------------------------------
This means a configuration where painter 1 paints boards 1 and 3 but not 2 is invalid.

Return the ans % 10000003.

"""

class PaintersPartition:

    def solution(self, A:int, B: int, C: list[int]):

        # Search space: Max of C element * B to Sum of all C elements * B
        total = 0
        maxi = float('-inf')

        for board in C:

            maxi = max(maxi, board)
            total += board

        low = maxi * B 
        high = total * B 
        ans = 0
        while (low <= high):

            mid = low + (high-low)//2

            if self.painters(C, mid, B) <= A:
                ans = mid
                high = mid -1
            else:
                low = mid + 1

        return ans

    def painters(self, boards: list[int], alloted_time: int, unit: int)-> int:
        """
        Algorithm
        -----------------------------------------
        1. Iterate over the boards and for each board find total time required to paint it.
        2. Check whether current painter has enough time to paint it.
        3. If not assign the board to next painter
        4. Return the total painters count.

        Time and Space Complexity
        ------------------------------
        TC: O(n) and SC: O(1)
        
        """

        count = 1

        time_left = alloted_time - boards[0] * unit

        for i in range(1, boards.__len__()):

            required_time = boards[i] * unit

            if (time_left < required_time):
                # Assign a new painter and allot the board to it
                count += 1
                time_left = alloted_time - required_time
            else:
                time_left -= required_time

        return count
    
if __name__ == "__main__":

    pp =  PaintersPartition()

    # Test Case 1:
    A = 10
    B = 1
    C = [1, 8, 11, 3]
    print("Minimum required time: ", pp.solution(A, B, C))

    # Test case 2:
    A = 1
    B = 1000000
    C = [1000000,1000000]
    print("Minimum required time: ", pp.solution(A, B, C))

