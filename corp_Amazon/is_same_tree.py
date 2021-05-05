class Solution:
    def is_same_tree(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        return p.val == q.val and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

# 1st if
# if both are NULL, both have reached the leaf nodes

# 2nd if
# if one is NULL and the other is not (since 1st check covered the case where both are none), then clearly aint the same tree

# 1st and 2nd IFs are the exit condition for recursion
# finally, if current values are the same btw the two and the relationship is recursively true for both sub nodes, then the tree must be the same
