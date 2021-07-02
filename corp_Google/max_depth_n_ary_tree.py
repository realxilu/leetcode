class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        _max = 0
        for c in root.children:
            _max = max(_max, self.maxDepth(c))

        return _max + 1

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
