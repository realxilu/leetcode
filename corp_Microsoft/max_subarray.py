class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0)

        return max(dp)

# if the prev dp value is less than zero we don't take it, otherwise we take the value
