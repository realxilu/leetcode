from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res, q, flag = [], deque([root]), True
        while q:
            lvl, lvl_len = [], len(q) # <--- this is the most important part
            for _ in range(lvl_len):
                node = q.popleft()
                lvl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if flag:
                res.append(lvl)
            else:
                res.append(lvl[::-1])
            flag = not flag

        return res

# [KEY] level order => BFS
# Add an additional for-loop before pushing children into the queue 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
