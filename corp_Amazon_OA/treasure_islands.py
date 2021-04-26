class Solution:
    def __init__(self):
        self.m, self.n, self.min_ = len(grid), len(grid[0]), float('inf')

    def treasure_island(self, grid):
        if not grid:
            return -1

        self.dfs(grid, 0, 0, 0)

        return self.min_

    def dfs(self, grid, i, j, step):
        if not (0 <= i < self.m) or not (0 <= j < self.n) or grid[i][j] == 'D':
            return

        if grid[i][j] == 'X':
            self.min_ = min(self.min_, step)
            return

        step += 1

        grid[i][j] = 'D'

        self.dfs(grid, i + 1, j, step)
        self.dfs(grid, i - 1, j, step)
        self.dfs(grid, i, j + 1, step)
        self.dfs(grid, i, j - 1, step)

        grid[i][j] = 'O'


# driver
s = Solution()
grid = [['O', 'O', 'O', 'O'],
        ['D', 'O', 'D', 'O'],
        ['O', 'O', 'O', 'O'],
        ['X', 'O', 'O', 'O']]
ss = s.treasure_island(grid)
print(ss)
