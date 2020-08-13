# TODO: BUG!
class Solution:
    def maxLevelSum(self, root):
        if root is None:
            None

        q, min_, level, min_level = [root], float('inf'), 0, float('inf')
        while len(q):
            len_ = len(q)
            sum_ = 0
            for x in range(len_):
                node = q.pop(0)
                sum_ += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if sum_ < min_:
                min_ = sum_
                min_level = level

            level += 1

        return min_level


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
