class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        res, dic = [], {}

        dic['2'] = 'abc'
        dic['3'] = 'def'
        dic['4'] = 'ghi'
        dic['5'] = 'jkl'
        dic['6'] = 'mno'
        dic['7'] = 'pqrs'
        dic['8'] = 'tuv'
        dic['9'] = 'wxyz'

        self.backtrack('', digits, res, dic)

        return res

    # recusrive backtrack
    def backtrack(self, combo, digits, res, dic):
        # exit condition
        if len(digits) == 0:
            res.append(combo)
            return
        
        digit = digits[0]
        letters = dic[digit]

        # explore other path using recursion
        for c in letters:
            self.backtrack(combo + c, digits[1:], res, dic)
