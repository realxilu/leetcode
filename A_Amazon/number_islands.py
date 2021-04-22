# note '1' is island, '0' is visisted
class Solution:
    def numIslands(self, grid):
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # erase all reachable islands from the current grid
                    self.dfs(grid, i, j)
                    # the whole chunk of 1s is considered 1 island
                    count += 1

        return count

    def dfs(self, grid, i, j):
        # If out of bound. Note the 'not' keyword here.
        if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])) or grid[i][j] == '0':
            return  # this is the part where the function backtracks

        # mark the current cell visisted
        grid[i][j] = '0'

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
