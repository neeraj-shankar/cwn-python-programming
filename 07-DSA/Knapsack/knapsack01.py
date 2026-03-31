"""
Given two integer arrays A and B of size N each which represent values and weights associated with N 
items respectively.

Also given an integer C which represents knapsack capacity.

Find out the maximum value subset of A such that sum of the weights of this subset is smaller 
than or equal to C.

NOTE:
You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
"""

class Knapsack:

    def solution_tda(self, A: list[int], B: list[int], C: int)-> int:
        n = len(A)
        memo = [[-1 for _ in range(C+1)] for _ in range(n)]
        print(memo)
        return self.knapsack(B, A, C, 0, memo)

    def knapsack(self, weights: list[int], values: list[int], capacity: int, idx: int, memo: list[int]):

        # Base Case: When all values visited
        if idx == len(values) or capacity <= 0:
            return 0
        
        if memo[idx][capacity] != -1:
            return memo[idx][capacity]
        
        skip = self.knapsack(weights, values, capacity, idx+1, memo)

        pick = 0
        if weights[idx] <= capacity:
            pick = self.knapsack(weights, values, capacity - weights[idx], idx+1, memo) + values[idx]
        
        memo[idx][capacity] = max(pick, skip)
        return memo[idx][capacity]


if __name__ == "__main__":

    ks = Knapsack()

    A = [60, 100, 120]
    B = [10, 20, 30]
    C = 50
    print(f"Maximum Values: {ks.solution_tda(A, B, C)}")

    A = [10, 20, 30, 40]
    B = [12, 13, 15, 19]
    C = 10
    print(f"Maximum Values: {ks.solution_tda(A, B, C)}")
