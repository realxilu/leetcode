class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.a = None
        self.b = None
        self.prev = TreeNode(float('-inf'))

    def recoverTree(self, root: TreeNode) -> None:
        self.traverse(root)

        self.a.val, self.b.val = self.b.val, self.a.val

    # [RECURSIVE]
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

# [ITERATIVE][STACK]
def recoverTree(self, root):
    cur, prev, records, stack = root, TreeNode(float('-inf')), [], []
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        node = stack.pop()
        
        # If nodes are out of place
        if prev.val > node.val:
            # record the current out of place couple
            records.append((prev, node))
        prev, cur = node, node.right

    # out of order nodes are ajacent
    if len(records) == 1: 
        records[0][0].val, records[0][1].val = records[0][1].val, records[0][0].val
    # out of order nodes are not ajacent
    else:
        records[0][0].val, records[1][1].val = records[1][1].val, records[0][0].val

# [TODO] Morris