"""
Rishik likes candies a lot. So, he went to a candy-shop to buy candies.

The shopkeeper showed him N packets each containg A[i] candies for cost of C[i] nibbles, each candy in that packet has a sweetness B[i]. The shopkeeper puts the condition that Rishik can buy as many complete candy-packets as he wants but he can't buy a part of the packet.

Rishik has D nibbles, can you tell him the maximum amount of sweetness he can get from candy-packets he will buy?


Problem Constraints
---------------------------------------------------------------------
1 <= N <= 700
1 <= A[i] <= 1000
1 <= B[i] <= 1000
1 <= C[i],D <= 1000
"""

class BuyingCandies:

    def solution_tda(self, A: list[int], B: list[int], C: list[int], D: int):

        memo = [[-1] * (D+1) for _ in range(len(A))]

        return self.knapsack(A, B, C, 0, D)

    def knapsack(self, packets: list[int], sweatness: list[int], cost: list[int], idx: int, rem: int):

        # Base Case: 
        if idx == len(packets) or rem < 0:
            return 0
        

        skip = self.knapsack(packets, sweatness, cost, idx+1, rem)

        pick = 0
        current_cost = packets[idx] * cost[idx]
        if current_cost <= rem:
            pick = self.knapsack(packets, sweatness, cost, idx, rem-current_cost) + (packets[idx] * sweatness[idx])
        
        return max(skip, pick)

if __name__ == "__main__":

    bc = BuyingCandies()

    # Test Case 1:
    A = [1, 2, 3]
    B = [2, 2, 10]
    C = [2, 3, 9]
    D = 8
    print(f"Maximum sweatness: {bc.solution_tda(A, B, C, D)}")