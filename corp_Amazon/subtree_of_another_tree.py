class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False

        if self.is_identical(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_identical(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        return self.is_identical(root1.left, root2.left) and self.is_identical(root1.right, root2.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
