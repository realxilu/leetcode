class Solution:
    def flatten(self, root):
        if root is None:
            return

        old_left = root.left
        old_right = root.right

        root.left = None

        self.flatten(old_left)
        self.flatten(old_right)

        root.right = old_left

        cur = root
        while cur.right:
            cur = cur.right

        cur.right = old_right


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
