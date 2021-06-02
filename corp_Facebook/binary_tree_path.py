class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        res, tmp = [], []
        self.binaryTreePathsHelper(root, res, tmp)

        return ['->'.join(x) for x in res]

    def binaryTreePathsHelper(self, root, res, tmp):
        if not root:
            return

        val = str(root.val)

        if not root.left and not root.right:
            res.append(tmp + [val])

        if root.left:
            self.binaryTreePathsHelper(root.left, res, tmp + [val])

        if root.right:
            self.binaryTreePathsHelper(root.right, res, tmp + [val])

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
