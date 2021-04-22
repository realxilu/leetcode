class Solution:
    def two_sum(self, nums, target):
        dic = {}

        for i, x in enumerate(nums):
            if target - x in dic:
                return dic[target - x], i

            dic[x] = i

        return None
