class Solution:
    # [BEST]
    def coinChange(self, coins, amount):
        n = len(coins)
        dp = [0] + [float('inf')] * amount

        # build table bottom up: $1, $2, $3 ... $x
        for x in range(1, amount + 1):
            # check each denomination
            for i in range(n):
                if coins[i] <= x:
                    # either use or not use the coin
                    dp[x] = min(dp[x], dp[x - coins[i]] + 1)

        return -1 if dp[amount] > amount else dp[amount]


class Solution:
    # [DO_NOT_USE][GREEDY]: this ONLY works for certain coin denomiation: 1, 5, 10, 50
    def coinChange(self, coins, amount):
        coins.sort()
        count, i = 0, len(coins) - 1

        while amount and i >= 0:
            if coins[i] <= amount:
                count += amount // coins[i]
                amount %= coins[i]
            i -= 1

        return -1 if amount > 0 else count
