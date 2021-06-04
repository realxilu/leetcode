class Solution:
    def invertTree(self, root):
        if not root:
            return None

        # record root.right since it would be modified
        old_right = root.right

        root.right = self.invertTree(root.left)
        root.left = self.invertTree(old_right)

        return root

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
