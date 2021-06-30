class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return False

        # inner function ---------------------
        def inOrder(root, s, target):
            if not root:
                return

            inOrder(root.left, s, target)
            s.add(target - root.val)
            inOrder(root.right, s, target)
        # ----------------------------------------

        s = set()
        inOrder(root1, s, target)

        cur, stack = root2, []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if node.val in s:
                return True
            cur = node.right

        return False

# [KEY] traverse the first tree, build a set using target - node.val
# traverse the second tree to see if any element exists in the set

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
