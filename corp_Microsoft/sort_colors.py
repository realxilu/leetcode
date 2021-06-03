class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if not nums:
            return

        i, j = 0, len(nums) - 1

        for k in range(len(nums)):
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1

        for k in range(len(nums)-1, -1, -1):
            if nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1

# [MY_OWN_SOLUTION]