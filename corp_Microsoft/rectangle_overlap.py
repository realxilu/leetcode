class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1[0], rec1[1], rec1[2], rec1[3]
        x3, y3, x4, y4 = rec2[0], rec2[1], rec2[2], rec2[3]

        return not (x2 <= x3 or y4 <= y1 or x4 <= x1 or y2 <= y3)

# [KEY] [1-D] [NEED TO DRAW] [DeMorgan]
