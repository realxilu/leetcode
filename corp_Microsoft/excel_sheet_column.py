class Solution:
    def titleToNumber(self, string: str) -> int:
        if not string:
            return -1

        res = 0
        for c in string:
            res *= 26 # 26 base
            res += ord(c) - ord('A') + 1

        return res

# ord: convert alphabet to number
# chr: convert number to alphabet

# use similar logic but base 26
# 724 in base 10
# 0 * 10 + 7 = 7
# 7 * 10 + 2 = 72
# 12 * 10 + 4 = 124