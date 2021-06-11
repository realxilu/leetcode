class Solution:
    def convertToTitle(self, num: int) -> str:
        # wanted A to Z but don't wanna type them out
        alphabet = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        res = []

        # 26-based number
        while num:
            # alphabet is 0-based thus num - 1 here
            # % 26 will yield the least significant digit in 26 base
            res.append(alphabet[(num - 1) % 26])
            # integer division will move the digit forward, since we have already handled the last digit here (think in base 10)
            num = (num - 1) // 26

        # [ATTENTION] to reverse because function 'append' was used
        return ''.join(res)[::-1]

# [KEY] think in base 10 and then convert to base 26
# 123 % 10 = 3
# 123 // 10 = 12
# --------------
# 12 % 10 = 2
# 12 // 10 = 1
# --------------
# 1 % 10 = 1 
# 1 // 10 = 0

# [PYTHON]
# ord: convert alphabet to number
# chr: convert number to alphabet
