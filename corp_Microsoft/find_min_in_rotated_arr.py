class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        if len(nums) == 1:
            return nums[0]

        return self.search_min(nums, 0, len(nums) - 1)

    def search_min(self, nums, lo, hi):
        mid = (lo + hi) // 2

        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        if mid == 0:
            return nums[0]

        if nums[mid] > nums[-1]:
            return self.search_min(nums, mid, hi)
        else:
            return self.search_min(nums, lo, mid)
