# TODO: BUG!
class Solution:
    def subarray_sum(self, nums, k):
        sum_, res = 0, 0
        dic = {}
        dic[0] = 1

        for x in range(len(nums)):
            sum_ += x

            if sum_ - k in dic:
                res += dic[sum_ - k]

            dic[sum_] = (dic.get(sum_) or 0) + 1

        return res
