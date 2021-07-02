class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_min_depth = self.minDepth(root.left)
        right_min_depth = self.minDepth(root.right)

        if left_min_depth == 0 and right_min_depth == 0:
            return 1

        if left_min_depth == 0:
            return right_min_depth + 1

        if right_min_depth == 0:
            return left_min_depth + 1

        return min(left_min_depth, right_min_depth) + 1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
