class Solution:
    def max_number_of_balloons(self, text):
        if text is None:
            return 0

        dic = { 'b': 0,
                'a': 0,
                'l': 0,
                'o': 0,
                'n': 0 }

        for c in text:
            if c in dic:
                dic[c] += 1

        dic['l'] //= 2
        dic['o'] //= 2

        min_ = float('inf')
        for c in dic:
            min_ = min(min_, dic[c])

        return min_
