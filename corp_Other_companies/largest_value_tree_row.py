from collections import deque

def largestValuesInTreeRows(root):
    if not root:
        return []

    res, q = [], deque([root])
    while q:
        level, lvl_len = [], len(q)
        for _ in range(lvl_len):
            node = q.popleft()
            level.append(node.value)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        row_max = max(level)
        res.append(row_max)

    return res

# [KEY] review level based traversal, lvl_len should be recorded for each row
# \leetcode\code_signal\largest_value_tree_row.py


class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
