class Solution:
    def num_islands(self, grid):
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # erase all reachable islands from the current grid
                    self.dfs(grid, i, j)
                    count += 1

        return count

    def dfs(self, grid, i, j):
        # out of bound
        if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])) or grid[i][j] == '0':
            return

        # mark visited
        grid[i][j] = '0'

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
