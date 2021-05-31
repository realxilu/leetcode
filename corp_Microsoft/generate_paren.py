class Solution:
    def generateParenthesis(self, n):
        res = []
        self.backtrack(res, '', 0, 0, n)

        return res

    def backtrack(self, res, string, _open, close, _max):
        if len(string) == _max * 2:
            res.append(string)
            return

        if _open < _max:
            self.backtrack(res, string + '(', _open + 1, close, _max)

        if close < _open:
            self.backtrack(res, string + ')', _open, close + 1, _max)
