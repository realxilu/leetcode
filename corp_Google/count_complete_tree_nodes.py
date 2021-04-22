from collections import deque


class Solution:
    def count_nodes(self, root):
        if root is None:
            return 0

        q, count = deque([root]), 0
        while q:
            node = q.popleft()
            count += 1

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return count


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
