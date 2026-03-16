"""
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

"""


class CoinChange:
    total_iterations = 0
    def solve_tda(self, coins: list[int], target: int)-> int:
        dp = [-1 for _ in range(target+1)]
        total = self.combination(coins, target, dp)
        if total == float('inf'):
            return -1

        return total 

    def combination(self, coins: list[int], rem: int, dp: list[int]):

        if rem == 0:
            return 0
        
        if rem < 0:
            return float('inf')
        
        if dp[rem] != -1:
            return dp[rem]
        
        ans = float('inf')
        for i in range(0, len(coins), 1):
            self.total_iterations += 1
            res = self.combination(coins, rem - coins[i], dp)
            ans = min(ans, res + 1)

        dp[rem] = ans
        return dp[rem]
    
    def solve_tabular(self, coins: list[int], amount: int)-> int:

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        n = len(dp)
        for i in range(1, n, 1):
            for coin in coins:
                if i - coin >=0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
        
if __name__ == "__main__":

    cc = CoinChange()
    coins = [186,419,83,408]
    amount = 6249

    print(f"Minimum Coins required: {cc.solve_tda(coins, amount)}")
    print(cc.total_iterations)
    print(f"Minimum Coins required Tabular: {cc.solve_tabular(coins, amount)}")



