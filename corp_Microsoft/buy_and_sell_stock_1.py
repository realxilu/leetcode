class Solution:
    def max_profit(self, prices):
        _min, _max = float('inf'), -float('inf')

        for x in prices:
            _min = min(_min, x)
            _max = max(_max, x - _min)

        return _max if _max > 0 else 0
