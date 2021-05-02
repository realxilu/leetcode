class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return None

        tmp = 1
        res = len(nums) * [1]

        for i in range(len(nums) - 1):
            tmp *= nums[i]
            res[i + 1] = tmp

        tmp = 1
        for i in range(len(nums) - 1, 0, -1):
            tmp *= nums[i]
            res[i - 1] = tmp * res[i - 1]

        return res
