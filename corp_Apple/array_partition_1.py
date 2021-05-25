class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

# [KEY] if a small number is grouped with a biggest number, it would waste the potential of the biggest number
# thus sorting the input array would help
# [1,2] [3,4] => 1 + 3
# [1,4] [2,3] => 1 + 2
# [1,3] [2,4] => 1 + 2
