class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if not p:
            return False
        if not q:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1-IF
# if both are NULL, both have reached the leaf nodes

# 2-IF
# if one is NULL and the other is not (since 1st check covered the case where both are none), then clearly aint the same tree

# 1) and 2) IFs are the exit conditions for recursion
# finally, if current values are the same between the two and the relationship is recursively true for both sub nodes, 
# then the tree must be the same
