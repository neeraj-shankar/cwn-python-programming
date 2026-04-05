"""
Say you have an array, A, for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.

You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class BuySellStockII:

    def solution(self, stocks:list[int]):

        n = len(stocks)

        ans = 0

        for i in range(1, n):

            if stocks[i] > stocks[i-1]:
                profit = stocks[i] - stocks[i-1]
                ans += profit

        return ans
if __name__ == "__main__":

    bss = BuySellStockII()

    A = [1, 2, 3]
    print(f"Total Profit: {bss.solution(A)}")

    A = [5, 2, 10]
    print(f"Total Profit: {bss.solution(A)}")

