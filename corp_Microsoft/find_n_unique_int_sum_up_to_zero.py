class Solution:
    def sumZero(self, n: int) -> List[int]:
        return range(1 - n, n, 2)

# [key] observe following mathmatical property
# n = 1, [0]
# n = 2, [-1, 1]
# n = 3, [-2, 0, 2]
# n = 4, [-3, -1, 1, 3]
# n = 5, [-4, -2, 0, 2, 4]
