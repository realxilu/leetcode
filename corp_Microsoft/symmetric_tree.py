class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.is_symmetric(root.left, root.right)

    def is_symmetric(self, left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val != right.val:
            return False

        return self.is_symmetric(left.left, right.right) and self.is_symmetric(left.right, right.left)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# [KEY] the helper function took two arguments instead of one!

# The following code is very elegant but harder to read espeically under stress
# if not left or not right:
#     return left is right

# Code translation:
# if at least 1 child doesn't exist:
# 1) neither exits/both None, then both are None so left is right
# 2) if that is not the case then the tree is asymetrical