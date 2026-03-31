"""
The monetary system in DarkLand is really simple and systematic. 
The locals-only use coins. The coins come in different values. The values used are:

 1, 5, 25, 125, 625, 3125, 15625, ...
Formally, for each K >= 0 there are coins worth 5K.

Given an integer A denoting the cost of an item, find and return the smallest number of coins 
necessary to pay exactly the cost of the item (assuming you have a sufficient supply of coins of 
each of the types you will need).
"""

class AnotherCoinPrblem:

    def solve_greedy(self, A):

        total_coins = 0

        while A > 0:

            rem = A % 5
            total_coins += rem 
            A = A//5

        return total_coins

if __name__ == "__main__":

    acp = AnotherCoinPrblem()

    # Test Case 1: 
    A = 47
    print(f"Minimum number of coins needed: {acp.solve_greedy(A)}")

    # Test Case 2: 
    A = 9
    print(f"Minimum number of coins needed: {acp.solve_greedy(A)}")


    # Test Case 3: 
    A = 100
    print(f"Minimum number of coins needed: {acp.solve_greedy(A)}")