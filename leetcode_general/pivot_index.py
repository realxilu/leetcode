class Solution:
    def pivot_index(self, nums):
        if not nums:
            return -1

        left, right = 0, sum(nums)

        for i, x in enumerate(nums):
            right -= x

            if left == right:
                return i

            left += x

        return -1
