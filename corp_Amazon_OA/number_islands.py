# '1' is land
# '0' is water or visisted
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
        # 1) out of bound
        # 2) hit water
        if not ((0 <= i < len(grid)) and (0 <= j < len(grid[0]))) or grid[i][j] == '0':
            return  # backtrack

        # do visit and mark the cell water
        grid[i][j] = '0'

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


# [KEY] run dfs from each node in the map