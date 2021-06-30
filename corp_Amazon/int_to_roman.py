class Solution:
    def intToRoman(self, num):
        digits = [1000, 900, 500, 400,  100,  90,   50,  40,  10,    9,   5,    4,    1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        res = ''
        for digit, roman in zip(digits, romans):
            res += (num // digit) * roman
            num = num % digit

        return res

# [KEY] modulous operation

# [IMPORTANT] 
# 0 * 'CM' = ''
# 3 * 'IV' = 'IVIVIV'

# Dry run following [EXAMPLE]

# num = 743
# 743 // 1000, 743 // 900, 743 // 500 = 1, ....
# res = D
# 743 % 500 = 243

# num = 243
# 243 // 1000, ..., 243 // 100 = 2, ...
# res = DCC
# ..., 243 % 100 = 43, ...

# num = 43
# 43 // 1000, ... 43 // 40 = 1, ...
# res = DCCXL
# 43 % 40 = 3

# num = 3
# ..., 3 // 1 = 3
# res = DCCXLIII
