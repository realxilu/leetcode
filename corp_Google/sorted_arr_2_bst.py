class Solution:
    def sortedArrayToBST(self, num):
        if not num:
            return num

        return self.sortedArray2Bst(num, 0, len(num) - 1)

    def sortedArray2Bst(self, num, lo, hi):
        if lo > hi:
            return None

        mid = lo + (hi - lo) // 2 # (lo + hi) // 2
        root = TreeNode(num[mid])

        root.left = self.sortedArray2Bst(num, lo, mid - 1)
        root.right = self.sortedArray2Bst(num, mid + 1, hi)

        return root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
