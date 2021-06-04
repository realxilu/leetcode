class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        begin = i = 0

        while i < len(nums):
            if nums[i] != val:
                nums[begin] = nums[i]
                begin += 1
            i += 1

        return begin
