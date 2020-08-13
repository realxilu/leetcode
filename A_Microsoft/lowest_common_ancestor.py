class Solution:
    def lowest_common_ancestor(self, root, p, q):
        if root is None:
            return None

        if root is p or root is q:
            return root

        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
