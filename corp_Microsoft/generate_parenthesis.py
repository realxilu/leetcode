class Solution:
    def generateParenthesis(self, n):
        res = []
        self.backtrack(res, '', 0, 0, n)

        return res

    def backtrack(self, res, tmp, _open, _close, _max):
        if len(tmp) == _max * 2:
            res.append(tmp)
            return

        if _open < _max:
            self.backtrack(res, tmp + '(', _open + 1, _close, _max)

        if _close < _open:
            self.backtrack(res, tmp + ')', _open, _close + 1, _max)

# [KEY][BACKTRACK]
# _open: count number of open bracket
# _close: number of _close bracket count
# _max: max allowable bracket
# tmp: string in the making
# res: the shared overall result set