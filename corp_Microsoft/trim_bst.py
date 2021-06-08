class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        if root.val > high:
            return root.left

        if root.val < low:
            return root.right

        return root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
