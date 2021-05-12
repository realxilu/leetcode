class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        
        step = 0
        while fresh:
            if not rotting:
                return -1
            
            # compute rotten orange using directional vectors
            rotting = { (i + di, j + dj) for i, j in rotting for di,
                       dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i+di, j+dj) in fresh }
            fresh -= rotting
            step += 1
        
        return step
