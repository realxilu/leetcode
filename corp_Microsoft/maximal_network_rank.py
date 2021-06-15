class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connected, counts = [[False for _ in range(n)] for _ in range(n)], [0] * n

        for r in roads:
            counts[r[0]] += 1
            counts[r[1]] += 1
            connected[r[0]][r[1]] = True
            connected[r[1]][r[0]] = True

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, counts[i] + counts[j] -
                          (1 if connected[i][j] else 0))

        return res
