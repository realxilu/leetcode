class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        _max = 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
