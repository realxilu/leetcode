class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return None

        i, j = 0, len(nums) - 1

        res = []
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                res.append(nums[i] ** 2)
                i += 1
            else:
                res.append(nums[j] ** 2)
                j -= 1

        return res[::-1]

# [BT][TWO_POINTER]