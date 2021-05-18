
class Solution:
    def calculate_minimum_HP(self, dungeon):
        MAX = float('inf')

        m, n = len(dungeon), len(dungeon[0])

        dp = [[MAX] * (n + 1) for i in range(m + 1)]

        dp[m][n - 1], dp[m - 1][n] = 1, 1

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = 1 if need <= 0 else need

        return dp[0][0]

# [KEY] dp[i][j] = minimal HP needed at grid (i, j)
# 1) Go from bottom right back to the origin
# 2) In order to survive, the knight needs to have at least 1 HP at the end
# 3) require extra space to hold dp

