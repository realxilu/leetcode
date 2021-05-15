class Solution(object):
    def myAtoi(self, s):
        digits = list(s.strip())

        if len(digits) == 0:
            return 0

        sign = -1 if digits[0] == '-' else 1

        if digits[0] in ('-', '+'):
            del digits[0]

        ret, i = 0, 0
        while i < len(digits) and digits[i].isdigit():
            ret = ret * 10 + int(digits[i])
            i += 1

        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))

# [REQUIREMENT]
# If the integer is out of the 32-bit signed integer range[-231, 231 - 1], 
# then clamp the integer so that it remains in the range. 
# Specifically, integers less than - 231 should be clamped to - 231, 
# and integers greater than 231 - 1 should be clamped to 231 - 1
