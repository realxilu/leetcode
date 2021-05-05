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

        string = string.replace('IV', 'IIII')
        string = string.replace('IX', 'VIIII')
        string = string.replace('XL', 'XXXX')
        string = string.replace('XC', 'LXXXX')
        string = string.replace('CD', 'CCCC')
        string = string.replace('CM', 'DCCCC')

        res = 0
        for c in string:
            res += dic[c]

        return res
