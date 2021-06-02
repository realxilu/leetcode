class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        # if the current root is p or q, then the current node is the LCA
        if root is p or root is q:
            return root

        # recursively check the left and right sub tree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if both are non null then apparently this cur is the LCA
        if left and right:
            return root

        # if left is non null and right null then LCA is left. Vice versa.
        return left if left else right

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
