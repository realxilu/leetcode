class Solution:
    def is_isomorphic(self, s, t):
        d1, d2 = {}, {}

        for i, x in enumerate(s):
            if x not in d1:
                d1[x] = t[i]
            elif d1[x] != t[i]:
                return False

        for i, x in enumerate(t):
            if x not in d2:
                d2[x] = s[i]
            elif d2[x] != s[i]:
                return False

        return True
