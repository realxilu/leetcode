from collections import deque


class Solution:
    def convert_to_title(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        res = deque([])

        while num:
            res.appendleft(capitals[(num - 1) % 26])
            num = (num - 1) // 26

        return ''.join(res)
