class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1  # count

        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[x] = nums[i + 1]
                x += 1

        return x

# TODO revisit without looking at the solution