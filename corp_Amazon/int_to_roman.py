class Solution:
    def intToRoman(self, num):
        numeric_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        res = ''
        for digit, roman in zip(numeric_values, roman_numerals):
            res += (num // digit) * roman
            num %= digit

        return res

# [KEY] string multiplication
# 0 * 'a' = ''
# 3 * 'a' = 'aaa'
