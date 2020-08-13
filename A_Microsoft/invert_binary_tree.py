class Solution:
    def invert_tree(self, root):
        if root is None:
            return None

        # record root.right since it would be modified
        right = root.right

        root.right = self.invert_tree(root.left)
        root.left = self.invert_tree(right)

        return root


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
