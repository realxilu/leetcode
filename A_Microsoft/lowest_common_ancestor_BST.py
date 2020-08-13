class Solution:
    def lowest_common_ancestor(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowest_common_ancestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowest_common_ancestor(root.right, p, q)

        return root


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
