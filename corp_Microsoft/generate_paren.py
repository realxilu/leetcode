class Solution:
    def generateParenthesis(self, n):
        res = []
        self.backtrack(res, '', 0, 0, n)

        return res

    def backtrack(self, res, tmp_string, _open, close, _max):
        if len(tmp_string) == _max * 2:
            res.append(tmp_string)
            return

        if _open < _max:
            self.backtrack(res, tmp_string + '(', _open + 1, close, _max)

        if close < _open:
            self.backtrack(res, tmp_string + ')', _open, close + 1, _max)

# [KEY] understand what each parameters mean
# _open: count number of open bracket
# close: number of close bracket count
# _max: max allowable bracket
# tmp_string: string in the making
# res: the shared overall result set