class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])

        for x in nums:
            _len = len(res) # [KEY] record the current res length BEFORE making modifications
            for i in range(_len):
                res.append(res[i].copy())
            for i in range(_len):
                res[i].append(x)

        return res
