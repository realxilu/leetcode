class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic = {}
        for a in nums1:
            for b in nums2:
                dic[a + b] = dic.get(a + b, 0) + 1
        
        res = 0
        for c in nums3:
            for d in nums4:
                res += dic.get(-c - d, 0)
        
        return res

# similar to two sum