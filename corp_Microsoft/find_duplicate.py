class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for x in nums:
            if x in s:
                return x
            s.add(x)
            
        return -1