"""
Given a knapsack weight A and a set of items with certain value B[i] and weight C[i], 
we need to calculate maximum amount that could fit in this quantity.

This is different from classical Knapsack problem, here we are allowed to use unlimited 
number of instances of an item.
"""

class UnboundKnapsack:

    def solution_tda(self, A: int, B: list[int], C: list[int])-> int:
        
        memo = [[-1] * (A+1) for _ in range(len(B))]
        return self.knapsack(B, C, A, 0, memo)

    def knapsack2(self, values: list[int], weights: list[int], capacity: int, start: int):


        for i in range(start, len(values)):
            pass 

    def knapsack(self, values: list[int], weights: list[int], capacity: int, idx: int, memo: list[int]):


        # Base Case
        if idx == len(values) or capacity <= 0:
            return 0
        
        if memo[idx][capacity] != -1:
            return memo[idx][capacity]
        skip = self.knapsack(values, weights, capacity, idx+1, memo)

        pick = 0
        if weights[idx] <= capacity:
            pick = self.knapsack(values, weights, capacity-weights[idx], idx, memo) + values[idx]

        memo[idx][capacity] = max(skip, pick)
        return memo[idx][capacity]
    
if __name__ == "__main__":

    uk = UnboundKnapsack()

    # Test Case 1:
    A = 10
    B = [6, 7]
    C = [5, 5]
    print(f"Max Value Picked: {uk.solution_tda(A, B, C)}")

    # Test Case 2: 
    A = 8
    B = [10, 40, 50, 70]
    C = [1, 3, 4, 5]
    print(f"Max Value Picked: {uk.solution_tda(A, B, C)}")

    # Test case 3:
    A = 100
    B = [10, 30, 20]
    C = [5, 10, 15]
    print(f"Max Value Picked: {uk.solution_tda(A, B, C)}")


