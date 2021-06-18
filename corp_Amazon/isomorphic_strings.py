class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic1, dic2 = {}, {}
        for x, y in zip(s, t):
            if x not in dic1:
                dic1[x] = y
            else:
                if dic1[x] != y:
                    return False

            if y not in dic2:
                dic2[y] = x
            else:
                if dic2[y] != x:
                    return False

        return True
