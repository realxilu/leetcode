from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        def bfs(x, y):
            visited, q, steps = set(), deque([(0, 0)]), 0

            while q:
                cur_level_length = len(q)
                # level order traversal
                
                # the for loop has a finite length, thus it controls the level-based access precisely
                for _ in range(cur_level_length):
                    cur_x, cur_y = q.popleft()
                    if (cur_x, cur_y) == (x, y):
                        return steps

                    # queue up neighbors
                    for offset_x, offset_y in offsets:
                        next_x, next_y = cur_x + offset_x, cur_y + offset_y
                        if (next_x, next_y) not in visited:
                            visited.add((next_x, next_y))
                            q.append((next_x, next_y))

                # each level is considered a move
                steps += 1

        return bfs(x, y)

# [KEY][BFS][LEVEL-ORDER-TRAVERSAL]
# The key question here is that why adopt level by level exploration?
# The first level to be hit is the min step. Note higher levels wouldn't necessarily mean the potential destinations are in outer layers.
# The first level visit would create a 8 positioned circle. From the 8 positioned circle, we can visit a pla

# BFS level order traveral is a speical case of bfs. Need to memorize the formula code and understand it well.