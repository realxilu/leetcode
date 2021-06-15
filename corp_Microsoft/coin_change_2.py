class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for cur_amt in range(coin, amount + 1):
                dp[cur_amt] += dp[cur_amt - coin]

        return dp[amount]

# [KEY][DP]
# You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.
# [WANT] Return the _number of combinations_ that make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return 0.
