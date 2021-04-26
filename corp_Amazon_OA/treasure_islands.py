## PROBLEM STATEMENT
# You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

# Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in . The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

# X: treasure island
# O: ocean
# D: dangerous rock/reef

class Solution:
    def __init__(self, grid):
        self.m, self.n = len(grid), len(grid[0])
        self._min = float('inf')

    def treasure_island(self, grid):
        if grid == None:
            return -1

        self.dfs(grid, 0, 0, 0)

        return self._min

    def dfs(self, grid, i, j, step):
        # If out of bound OR stepped on 'D'/dangerous cell, then backtrack
        if not (0 <= i < self.m) or not (0 <= j < self.n) or grid[i][j] == 'D':
            return

        if grid[i][j] == 'X':
            self._min = min(self._min, step)
            return

        step += 1

        grid[i][j] = 'D'

        self.dfs(grid, i + 1, j, step)
        self.dfs(grid, i - 1, j, step)
        self.dfs(grid, i, j + 1, step)
        self.dfs(grid, i, j - 1, step)

        grid[i][j] = 'O'


# main
grid = [['O', 'O', 'O', 'O'],
        ['D', 'O', 'D', 'O'],
        ['O', 'O', 'O', 'O'],
        ['X', 'O', 'O', 'O']]
s = Solution(grid)
ss = s.treasure_island(grid)
print(ss)
