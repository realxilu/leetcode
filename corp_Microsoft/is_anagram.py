class Solution:
    def is_anagram(self, s, t):
        if len(s) != len(t):
            return False

        for x, y in zip(sorted(s), sorted(t)):
            if x != y:
                return False

        return True


class Solution:
    def is_anagram(self, s, t):
        if len(s) != len(t):
            return False

        dic = {}
        for x in s:
            dic[x] = dic.get(x) + 1 if dic.get(x) else 1

        for x in t:
            dic[x] = dic.get(x) - 1 if dic.get(x) else None

        return all(x == 0 for x in dic.values())
