class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return None

        n = len(nums)
        tmp = 1
        res = [1] * n

        # 0 to n - 2 inclusive
        for i in range(n - 1):
            tmp *= nums[i]
            res[i + 1] = tmp

        tmp = 1
        # n - 1 to 1 inclusive
        for i in range(n - 1, 0, -1):
            tmp *= nums[i]
            res[i - 1] = tmp * res[i - 1] # cross multiply the previously generated res array

        return res

# [KEY][BT] is to visualize the problem
# 1,        2,          3,          4
#           1           1*2         1*2*3
# 2*3*4     3*4         4           
