class Solution:
    def __init__(self):
        self.list_ = []

    def preorder(self, root):
        self._preorder(root, self.list_)

        return self.list_

    def _preorder(self, root, list_):
        if not root:
            return

        list_.append(root.val)

        for x in root.children:
            self._preorder(x, list_)


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
