# how to typically handle grid and its moving ops:

# direction [1 0] [0 1] [-1 0] [0 -1]
rotting = {(i+di, j+dj) for i, j in rotting for di,
           dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i+di, j+dj) in fresh}
