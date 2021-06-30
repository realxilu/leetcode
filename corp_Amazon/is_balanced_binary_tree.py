class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        left = self.depth(root.left)
        right = self.depth(root.right)

        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    # [KEY] helper function
    def depth(self, root):
        if not root:
            return 0

        return 1 + max(self.depth(root.left), self.depth(root.right))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
