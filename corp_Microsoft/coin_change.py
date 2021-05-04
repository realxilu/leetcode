# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, 

# return -1. You may assume that you have an infinite number of each kind of coin.

# ----------------------------------------------------------------------------------------------------

# x = current amount, for example 1 cent 2 cents .. 17 cents
# i = coin denomiation index

class Solution:
    # [BEST]
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf')] * amount # [0] is the base case, it takes 0 coin to change 0 coin

        # build table bottom up: $1, $2, $3 ... $x
        for x in range(1, amount + 1):
            # check each denomination
            for i in range(len(coins)):
                if coins[i] <= x:
                    # either use or not use the coin
                    dp[x] = min(dp[x], dp[x - coins[i]] + 1)

        return -1 if dp[amount] > amount else dp[amount]

# examples
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Input: coins = [2], amount = 3
# Output: -1

# Input: coins = [1], amount = 0
# Output: 0

# Input: coins = [1], amount = 1
# Output: 1

# Input: coins = [1], amount = 2
# Output: 2

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
