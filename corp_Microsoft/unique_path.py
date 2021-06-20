class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                mat[i][0], mat[0][j] = 1, 1

        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]

        return mat[m - 1][n - 1]

# [KEY][DP][IMAGE]