class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for cur_amt in range(coin, amount + 1):
                dp[cur_amt] += dp[cur_amt - coin]

        return dp[amount]
