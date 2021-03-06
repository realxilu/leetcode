from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None

        q, res = deque([root]), []
        while q:
            level, cur_level_len = [], len(q)

            # the key to [LEVEL-ORDER-TRAVERSAL] is to record the length of the current level so we won't over-queue
            for _ in range(cur_level_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    # queue neighbors
                    q.append(node.left)
                    q.append(node.right)

            if level:
                # record the rightmost element, [PY] '-1' is the index of the last element
                res.append(level[-1])
            # reset level - dump out the currently filled value for use in the next iteration
            level = []

        return res

# [KEY][BFS][LEVEL-ORDER-TRAVERSAL] Essentially this is just a level order traversal problem.
# The idea is to identify the last element (right view) of the level which by definition is the right side view
# Observation and analysis is important to solving this type of problems. But usually under the stress of interviews, one can hardly come up
# with an algorithm without any hint. Need to do more lc problems to gain proficency.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
