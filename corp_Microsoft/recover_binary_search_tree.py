class Solution:
    def __init__(self):
        self.a = None
        self.b = None
        self.prev = TreeNode(float('-inf'))

    def recoverTree(self, root: TreeNode) -> None:
        self.traverse(root)

        self.a.val, self.b.val = self.b.val, self.a.val

    def traverse(self, node):
        if not node:
            return

        self.traverse(node.left)

        if not self.a and self.prev.val > node.val:
            self.a = self.prev

        if self.a and self.prev.val > node.val:
            self.b = node

        self.prev = node

        self.traverse(node.right)

# [KEY] use global var 'a', 'b' to record nodes that are out of place. In in-order print, BST shall print in ascending order
# thus prev is less than the next