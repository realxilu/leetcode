class Solution:
    def is_same_tree(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        return p.val == q.val and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
