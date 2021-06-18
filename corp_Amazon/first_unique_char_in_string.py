class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1

        for i, c in enumerate(s):
            if dic[c] == 1:
                return i

        return -1
