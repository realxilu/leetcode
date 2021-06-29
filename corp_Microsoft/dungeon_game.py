class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])

        dp = [[float('inf')] * (n + 1) for i in range(m + 1)]

        dp[m][n - 1], dp[m - 1][n] = 1, 1

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = 1 if need <= 0 else need

        return dp[0][0]

# [KEY][DP] the knight needs at least 1 HP when he reaches the destination, then back out the initial hp from the origin
# dp[i][j] = minimal HP needed at grid (i, j)
# 1) Go from bottom right back to the origin
# 2) To survive, the knight needs to have _at least_ 1 HP at the destination
# 3) require 1 extra space to hold dp
