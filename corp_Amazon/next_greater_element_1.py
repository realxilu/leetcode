class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic, stack = {}, []

        for cur_num in nums2:
            while stack and stack[-1] < cur_num:
                dic[stack.pop()] = cur_num
            # stack adds a path
            stack.append(cur_num)

        return [dic.get(x, -1) for x in nums1]

# [KEY] use stack to keep track the path to the current element x
# if the peek is smaller than the current number x
# then peek's value's next greater element is x

# stack[-1] shows the last/top element of the array/stack
# stack[-1] is basically stack.peek() in Java
