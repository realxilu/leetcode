class Solution:
    def merge(self, intervals):
        # [IMPORTANT] sorted by the starting indices
        intervals = sorted(intervals, key=lambda x: x[0])

        # [innovative] usage of dummy
        res, pre = [], intervals[0]

        # intervals[1:] -> start from the 2nd element
        for x in intervals[1:]:
            # previous end is great than or touching the next interval's start
            if pre[1] >= x[0]:
                pre[1] = max(pre[1], x[1])
            else:
                res.append(pre)
                pre = x

        # don't forget the last case
        res.append(pre)

        return res
