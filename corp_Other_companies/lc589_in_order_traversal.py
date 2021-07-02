class Solution:
    def __init__(self):
        self._list = []

    def preorder(self, root):
        self._preorder(root, self._list)

        return self._list

    def _preorder(self, root, _list):
        if root is None:
            return

        _list.append(root.val)

        for x in root.children:
            self._preorder(x, _list)


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# https: // leetcode.com/problems/n-ary-tree-preorder-traversal/
