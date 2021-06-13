class Solution:
    def __init__(self):
        self.dic = {}
        self.dic['2'] = 'abc'
        self.dic['3'] = 'def'
        self.dic['4'] = 'ghi'
        self.dic['5'] = 'jkl'
        self.dic['6'] = 'mno'
        self.dic['7'] = 'pqrs'
        self.dic['8'] = 'tuv'
        self.dic['9'] = 'wxyz'

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        res = []
        self.backtrack('', digits, res)

        return res

    # recusrive backtrack
    def backtrack(self, combo, digits, res):
        # exit/base condition: when running out of digits then backtrack
        if len(digits) == 0:
            res.append(combo)
            return

        digit = digits[0]

        # explore other path using recursion
        # digits[1:] is a recurring pattern used to shrink the input size
        for c in self.dic[digit]:
            self.backtrack(combo + c, digits[1:], res)
