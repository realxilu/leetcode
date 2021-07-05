from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None

        res, q = [], deque([root])
        while q:
            lvl, lvl_len = [], len(q)
            for _ in range(lvl_len):
                node = q.popleft()
                lvl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(lvl)

        return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
