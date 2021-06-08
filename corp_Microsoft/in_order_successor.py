class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root or not p:
            return None

        # In a bst, if root.val > p.val it means p.val must be on the left subtree
        if root.val > p.val:
            # if can't find it in the left subtree, the root then must be the in order successor
            return self.inorderSuccessor(root.left, p) or root

        return self.inorderSuccessor(root.right, p)
