class Solution:
    def hasPathSum(self, t, s):
        if not t:
            return False

        if not t.left and not t.right:
            return t.val == s

        return self.hasPathSum(t.left, s - t.val) or self.hasPathSum(t.right, s - t.val)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
