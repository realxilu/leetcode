class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # i, j are indices pointing at the current char
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # if the current char of i and j are equal, the solution depends on i - 1 and j - 1's result
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # i - 1, j      ---> insert
                    # i    , j - 1  ---> delete
                    # i - 1, j - 1  ---> update
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[-1][-1]

# [KEY][DP] answer the question why insert, delete and update are represented the aforementioned indices
