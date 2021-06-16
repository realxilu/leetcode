class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = -1 if s[0] == '-' else 1
        if s[0] == '+' or s[0] == '-':
            s = s[1:]

        res = 0
        for c in s:
            if not c.isdigit():
                break
            res = 10 * res + int(c)

        return max(-2 ** 31, min(2 ** 31 - 1, sign * res))

# [REQUIREMENT]
# If the integer is out of the 32-bit signed integer range [-2**31, 2**31 - 1], 
# then clamp the integer so that it remains in the range.

# Specifically, integers less than - 2**31 should be clamped to - 2**31, 
# and integers greater than 2**31 - 1 should be clamped to 2**31 - 1
