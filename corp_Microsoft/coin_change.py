class Solution:
    # [BEST]
    def coin_change(self, coins, amount):
        dp = [0] + [float('inf')] * amount

        # try each amount
        for x in range(1, amount + 1):
            # check each denomination
            for i in range(len(coins)):
                if coins[i] <= x:
                    # either use or not use the coin
                    dp[x] = min(dp[x], dp[x - coins[i]] + 1)

        return -1 if dp[amount] > amount else dp[amount]


class Solution:
    # [ISSUE] [GREEDY]: this ONLY works for certain denomiation: 1, 5, 10, 50
    def coin_change(self, coins, amount):
        coins.sort()
        count, i = 0, len(coins) - 1

        while amount and i >= 0:
            if coins[i] <= amount:
                count += amount // coins[i]
                amount %= coins[i]
            i -= 1

        return -1 if amount > 0 else count
