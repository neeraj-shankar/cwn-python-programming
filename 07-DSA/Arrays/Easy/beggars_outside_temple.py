"""
There are A beggars sitting in a row outside a temple. Each beggar initially has an empty pot. 
When the devotees come to the temple, they donate some amount of coins to these beggars. 

Each devotee gives a fixed amount of coin(according to their faith and ability) to some K beggars sitting next 
to each other.

Given the amount P donated by each devotee to the beggars ranging from L to R index, where 1 <= L <= R <= A, 
find out the final amount of money in each beggar's pot at the end of the day, provided they don't fill 
their pots by any other means.

For ith devotee B[i][0] = L, B[i][1] = R, B[i][2] = P, given by the 2D array B

Problem Constraints
-----------------------------------------------------------
1 <= A <= 2 * 10^5
1 <= L <= R <= A
1 <= P <= 10^3
0 <= len(B) <= 10^5
"""

class BeggarsOutsideTemple():

    def solution_bruteforce(self, A: int, B: list) -> list:
        """
        1. Create a new empty array to store the total money to each beggar
        2. For every query in B, add the value from L to R index in the resultant array

        Time and Space Complexity
        ---------------------------------------------------
        TC: O(Q * N) --> N is length of resultant array, Q --> length of query array
        """
        pass 


    def solution_prefix_sum(self, A: int, B: list) -> list:
        """
        1. Create an empty array of size A and initialize its element with 0.
        2. For every L and R in query, add the P to the (L-1)th index and -P to (R-1)the index.
        3. Finally calculate the inplace prefix sum and return ans. 

        Time and space Complexity
        ---------------------------------------------------
        TC: (Q + N) 
        SC: N
        """
        ans = [0 for _ in range(A)]
        n = len(ans)
        # Iterate over each query and mark the presence
        for idx, num in enumerate(B):
            start = B[idx][0]
            end = B[idx][1]
            value = B[idx][2]

            ans[start-1] += value
            if end < n:
                ans[end] += -1 * value

        # Calculate the in place prefix sum
        for i in range(1, n, 1):
            ans[i] = ans[i-1] + ans[i]
        
        return ans




        

if __name__ == "__main__":

    # Create the class instance
    bot = BeggarsOutsideTemple()

    A = 5
    B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    print(f"Final output bruforce: {bot.solution_prefix_sum(A, B)}")
