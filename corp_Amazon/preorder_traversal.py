class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.preorder(root, res)

        return res

    def preorder(self, root, res):
        if not root:
            return

        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
