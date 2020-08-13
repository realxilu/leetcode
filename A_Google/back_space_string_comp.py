class Solution:
    def backspace_compare(self, s, t):
        return self.get_string(s) == self.get_string(t)

    def get_string(self, s):
        count, res = 0, []
        for x in reversed(s):
            if x == '#':
                count += 1
            elif count:
                count -= 1
            else:
                res.append(x)

        return ''.join(res)
