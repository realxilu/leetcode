import collections
class Solution:
    def findPairs(self, nums, k):
        res = 0
        dic = collections.Counter(nums)
        for key in dic:
            if k > 0 and key + k in dic or k == 0 and dic[key] > 1:
                res += 1

        return res

# if k == 0, the diff is 0 only when there are duplicates such that dic[key] > 1
# [KEY][DIC]
