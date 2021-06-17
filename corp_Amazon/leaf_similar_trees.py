class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1 = self._get_leaf_inorder(root1)
        l2 = self._get_leaf_inorder(root2)

        if len(l1) != len(l2):
            return False

        for x, y in zip(l1, l2):
            if x != y:
                return False

        return True

    def _get_leaf_inorder(self, root):
        cur, stack = root, []
        res = []

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if not node.left and not node.right:
                res.append(node.val)

            cur = node.right

        return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
