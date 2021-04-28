# 0: start
# 1: end
class Solution:
    def merge(self, intervals):
        # [IMPORTANT] sorted by the starting indices
        intervals = sorted(intervals, key=lambda x: x[0])

        # [innovative] usage of dummy
        res, pre = [], intervals[0]

        # note cur point starts at 2nd interval
        for cur in intervals[1:]:
            # pre's end is great than or touching the next interval's start
            if pre[1] >= cur[0]:
                pre[1] = max(pre[1], cur[1])
            else:
                res.append(pre)
                pre = cur

        # don't forget the last case
        res.append(pre)

        return res
