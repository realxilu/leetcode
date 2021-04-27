class Solution:
    def twoSum(self, nums, target):
        dic = {}

        for i, x in enumerate(nums):
            if target - x in dic:
                return dic[target - x], i

            # [KEY] look up the dictionary first and then add to dictionary to avoid double counting of the same index
            dic[x] = i

        return None
