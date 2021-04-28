class Solution:
    # most upvoted solution TODO needs a solution with better readability
    def max_area_of_island(self, grid):
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0

                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)

            return 0

        m, n = len(grid), len(grid[0])
        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]

        return max(areas) if areas else 0
