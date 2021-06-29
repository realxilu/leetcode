from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None

        q, res = deque([root]), []
        while q:
            # maintain a level variable and the current length
            level, cur_level_len = [], len(q)

            # the key to level order traveral is to record the length of the current level
            for _ in range(cur_level_len):
                node = q.popleft()
                if node:
                    # record the rightmost element
                    level.append(node.val)
                    # process bfs neighbors as usual only this is a binary tree
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level[-1])
            # reset level for it to be used in the next level
            level = []

        return res

# [KEY][BFS][LEVEL-ORDER-TRAVERSAL] Essentially this is just a level order traversal problem
# The idea is to print out the last element of the level which by definition is the right side view
# Observation and analysis is important to solving this type of questions. But usually under the stress of interviews, one can hardly come up
# with an algorithm without any hint. Need to do more lc problems to bypass this problem.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
