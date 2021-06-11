class Solution:
    def titleToNumber(self, string: str) -> int:
        if not string:
            return -1

        res = 0
        for c in string:
            res *= 26
            res += ord(c) - ord('A') + 1

        return res

# ord: convert alphabet to number
# chr: convert number to alphabet
