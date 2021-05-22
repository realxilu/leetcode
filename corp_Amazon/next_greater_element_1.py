class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic, stack = {}, []

        for x in nums2:
            while stack and stack[-1] < x:
                dic[stack.pop()] = x
            stack.append(x)

        return [dic.get(x, -1) for x in nums1]

# [KEY] use stack to keep track the path to the current element x
# if the peek is smaller than the current number x
# then peek's value's next greater element is x