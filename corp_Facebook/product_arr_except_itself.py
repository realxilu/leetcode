class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return None
        
        n = len(nums)
        tmp = 1
        res = [1] * n

        # [0, 1 ... n - 2]
        for i in range(n - 1):
            tmp *= nums[i]
            res[i + 1] = tmp

        tmp = 1
        # [n - 1, n - 2, ... 1]
        for i in range(n - 1, 0, -1):
            tmp *= nums[i]
            res[i - 1] = tmp * res[i - 1]

        return res
