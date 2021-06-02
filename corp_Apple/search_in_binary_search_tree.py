class Solution:
    def searchBST(self, root, val):
        if not root:
            return None

        if val == root.val:
            return root

        if val > root.val:
            return self.searchBST(root.right, val)

        if val < root.val:
            return self.searchBST(root.left, val)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
