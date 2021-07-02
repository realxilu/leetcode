class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0

        if low <= root.val <= high:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        # intentionally put this condition here for better readability
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
