class Solution:
    def merge(self, intervals):
        # [KEY] sorted by the starting indices
        intervals = sorted(intervals, key=lambda x: x[0])

        # [TIP] pre is a sentry/dummy
        res, pre = [], intervals[0]

        # [innovative] [1:] means start from the 2nd element(indexed as 1)
        for x in intervals[1:]:
            # previous(pre) end is great than or touching the current(x) start
            # pre[1] = pre's end; x[0] = x's start
            if pre[1] >= x[0]:
                pre[1] = max(pre[1], x[1])
            else:
                res.append(pre)
                pre = x

        # append the last interval
        res.append(pre)

        return res
