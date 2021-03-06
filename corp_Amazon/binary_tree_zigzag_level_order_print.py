from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res, q, flag = [], deque([root]), True
        while q:
            level, level_length = [], len(q) # <--- it's important to record the length
            for _ in range(level_length):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if flag:
                res.append(level)
            else:
                res.append(level[::-1])
            flag = not flag

        return res

# [KEY][BFS][LEVEL-ORDER-TRAVERSAL]
# Add an additional for-loop before pushing children into the queue 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
