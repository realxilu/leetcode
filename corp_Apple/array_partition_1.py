class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

# [KEY] if a small number is grouped with a biggest number, it would waste the potential of the biggest number
# thus sorting the input array would help