class Solution:
    def merge(self, intervals):
        # [IMPORTANT] must be sorted!
        intervals = sorted(intervals, key=lambda x: x[0])

        # NOTE pre starts at the first interval
        res, pre = [], intervals[0]

        # note cur pointer starts at the 2nd interval
        for cur in intervals[1:]:
            # pre's end is great than or touching the next interval's start
            if pre[1] >= cur[0]:
                pre[1] = max(pre[1], cur[1])
            else:
                res.append(pre)
                pre = cur

        # Don't forget to add the last interval
        res.append(pre)

        return res

# 0 = start
# 1 = end
