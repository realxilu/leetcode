class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        _max, index = self.get_max_index(nums)
        
        root = TreeNode(_max)
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])

        return root

    def get_max_index(self, nums):
        index, _max = -1, -float('inf')
        for i, x in enumerate(nums):
            if x > _max:
                _max, index = x, i

        return _max, index

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
