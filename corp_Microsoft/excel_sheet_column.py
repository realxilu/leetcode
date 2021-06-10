class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s:
            return -1

        res = 0
        for c in s:
            res *= 26
            res += ord(c) - ord(A) + 1
        
        return res

# ord: convert alphabet to number
# chr: convert number to alphabet
