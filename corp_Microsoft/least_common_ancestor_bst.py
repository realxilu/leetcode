class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        if q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return root

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
