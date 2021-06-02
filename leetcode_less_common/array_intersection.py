class Solution:
    def intersection(self, nums1, nums2):
        return set(nums1).intersection(nums2)


class Solution2:
    def intersection(self, nums1, nums2):
        s = set(nums1)

        res = set()
        for x in nums2:
            if x in s:
                res.add(x)

        return res
