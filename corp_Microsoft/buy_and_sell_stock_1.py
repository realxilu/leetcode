class Solution:
    def max_profit(self, prices):
        min_, max_ = float('inf'), -float('inf')

        for x in prices:
            min_ = min(min_, x)
            max_ = max(max_, x - min_)

        return max_ if max_ > 0 else 0
