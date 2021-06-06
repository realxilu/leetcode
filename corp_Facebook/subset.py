class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])

        for x in nums:
            _len = len(res)
            for i in range(_len):
                res.append(res[i].copy())
                i += 1

            for i in range(_len):
                res[i].append(x)

        return res
