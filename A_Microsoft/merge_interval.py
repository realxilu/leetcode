class Solution:
    def merge(self, intervals):
        if not intervals:
            return None

        # KEY sorted by the starting indices
        intervals = sorted(intervals, key=lambda x: x[0])

        res, pre = [], intervals[0]

        for x in intervals[1:]:
            # previous(pre) end is great than or touching the current(x) start
            if pre[1] >= x[0]:
                pre[1] = max(pre[1], x[1])
            else:
                res.append(pre)
                pre = x

        # append the last interval
        res.append(pre)

        return res
