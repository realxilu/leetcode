class Solution:
    def __init__(self):
        self.global_max = -float('inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path_down(root)

        return self.global_max

    def max_path_down(self, root):
        if not root:
            return 0

        left = max(0, self.max_path_down(root.left))
        right = max(0, self.max_path_down(root.right))

        # update the global max
        self.global_max = max(self.global_max, left + right + root.val)

        return max(left, right) + root.val

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
