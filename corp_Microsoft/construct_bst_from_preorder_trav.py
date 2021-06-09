import bisect

class Solution:
    def bstFromPreorder(self, A):
        # i, j are low and high indices
        def bst_preorder(i, j):
            if i > j:
                return None

            root = TreeNode(A[i])
            # bisect.bisect(a, x, lo=0, hi=len(a)) <==== NOTE 'hi' is the stop index you can reach, if u want the code to stop at j then put j+1
            mid = bisect.bisect(A, A[i], i + 1, j + 1)
            # bisect: The returned insertion point i partitions the array a into two halves so that all(val < x for val in a[lo:i])
            # for the left side and all(val >= x for val in a[i:hi]) for the right side.

            #  8     |   5      1      7   |      10        12    |  NO VALUE
            # A[i]     i + 1         mid-1        mid       j          j + 1
            root.left = bst_preorder(i + 1, mid - 1)
            root.right = bst_preorder(mid, j)

            return root

        return bst_preorder(0, len(A) - 1)

# NOTE bisect.bisect is only good for preorder-like arrays
# The code structure is preorder in nature

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
