class Solution:
    def romanToInt(self, string):
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # the ordering of following ops does NOT matter
        string = string.replace('IV', 'IIII')  # 4   = 5 - 1      = 1 + 1 + 1 + 1 
        string = string.replace('IX', 'VIIII') # 9   = 10 - 1     = 5 + 1 + 1 + 1 + 1
        string = string.replace('XL', 'XXXX')  # 40  = 50 - 10    = 10 + 10 + 10 + 10
        string = string.replace('XC', 'LXXXX') # 90  = 100 - 10   = 50 + 10 + 10 + 10 + 10
        string = string.replace('CD', 'CCCC')  # 400 = 500 - 100  = 100 + 100 + 100 + 100
        string = string.replace('CM', 'DCCCC') # 900 = 1000 - 100 = 500 + 100 + 100 + 100 + 100

        res = 0
        for c in string:
            res += dic[c]

        return res

# [KEY] string replacement for subtractive substrings