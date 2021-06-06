class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        _sum, count = 0, 0
        dic = {0: 1}

        for x in nums:
            _sum += x
            if _sum - k in dic:
                count += dic.get(_sum - k)

            dic[_sum] = dic.get(_sum, 0) + 1

        return count
