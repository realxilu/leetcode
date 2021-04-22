class Solution:
    def generate_parenthesis(self, n):
        res = []

        self.backtrack(res, '', 0, 0, n)

        return res

    def backtrack(self, res, string, open_, close, max_):
        if len(string) == max_ * 2:
            res.append(string)
            return

        if open_ < max_:
            self.backtrack(res, string + '(', open_ + 1, close, max_)

        if close < open_:
            self.backtrack(res, string + ')', open_, close + 1, max_)
