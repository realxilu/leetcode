class Solution:
    def intToRoman(self, num):
        numeric_values = [1000, 900, 500, 400,  100,  90,   50,  40,  10,    9,   5,    4,    1]
        roman_numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        res = ''
        for digit, roman in zip(numeric_values, roman_numerals):
            res += (num // digit) * roman
            num %= digit

        return res

# [KEY] modulous operation

# [IMPORTANT] 
# 0 * 'CM' = ''
# 3 * 'IV' = 'IVIVIV'

# [EXAMPLE] num = 743 as an
# 743 // 1000, 743 // 900, 743 // 500 = 1, ....
# res = D
# 743 % 500 = 243
# 243 // 1000, ... 243 // 100 = 2, ...
# res = DCC
# ... 243 % 100 = 43 ...
# 43 // 1000, ... 43 // 40 = 1, ...
# res = DCCXL
# 43 % 40 = 3
# ... 3 // 1 = 3
# res = DCCXLIII
# return DCCXLIII
