## PROBLEM STATEMENT
# You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

# Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in . The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

# X: treasure island
# O: ocean
# D: dangerous rock/reef

class Solution:
    def __init__(self, grid):
        self.m, self.n = len(grid), len(grid[0])
        # note this is a global/centralized min value, a min value every function stack can see
        self._min = float('inf')

    def treasure_island(self, grid):
        if grid is None:
            return -1

        self.dfs(grid, 0, 0, 0)

        return self._min

    def dfs(self, grid, i, j, step):
        # 1) hit the boundaries
        # 2) stepped on 'D'/dangerous cell
        if not (0 <= i < self.m) or not (0 <= j < self.n) or grid[i][j] == 'D':
            return # backtrack

        # if treasure is found
        if grid[i][j] == 'X':
            # compare current min with global min and update global min
            self._min = min(self._min, step)
            return

        step += 1

        # mark current cell as 'D'/dagerous 
        # why? marking a cell 'D' indicates it has been visisted, otherwise it will loop forever
        grid[i][j] = 'D'

        # let the code find its own path recursively
        self.dfs(grid, i + 1, j, step)
        self.dfs(grid, i - 1, j, step)
        self.dfs(grid, i, j + 1, step)
        self.dfs(grid, i, j - 1, step)

        # reinstate the cell as 'O'
        # [IMPORTANT] why do we need to recover the cell we marked 'D' early on?
        # 1) if the code is here, the original cell must be 'O', thus recovering. Only 3 options, if it were D or X the code could have returned already
        # 2) previously we used 'D' as 'visited', but after backtrack finished, this cell could be potentially be used for other dfs visits (that haven't happend yet, not returning it back to 'O' would have permanently altered the map)
        grid[i][j] = 'O'


# main
grid = [['O', 'O', 'O', 'O'],
        ['D', 'O', 'D', 'O'],
        ['O', 'O', 'O', 'O'],
        ['X', 'O', 'O', 'O']]
s = Solution(grid)
ans = s.treasure_island(grid)
print(ans)

