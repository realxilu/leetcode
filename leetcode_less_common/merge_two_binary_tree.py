import collections
# TODO: REVISIT


class Solution:
    def merge_trees(self, t1, t2):
        if not (t1 and t2):
            return t1 or t2

        q1, q2 = collections.deque([t1]), collections.deque([t2])
        while q1 and q2:
            n1, n2 = q1.popleft(), q2.popleft()
            if n1 and n2:
                n1.val = n1.val + n2.val
                if (not n1.left) and n2.left:
                    n1.left = TreeNode(0)
                if (not n1.right) and n2.right:
                    n1.right = TreeNode(0)

                q1.append(n1.left)
                q1.append(n1.right)
                q2.append(n2.left)
                q2.append(n2.right)

        return t1


class Solution:
    def merge_trees(self, t1, t2):
        if t1 is None and t2 is None:
            return None

        res = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))

        res.left = self.merge_trees(t1 and t1.left, t2 and t2.left)
        res.right = self.merge_trees(t1 and t1.right, t2 and t2.right)

        return res


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
