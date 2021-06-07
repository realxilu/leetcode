class Solution:
    def isValidBST(self, root, min_so_far=float('inf'), max_so_far=float('-inf')):
        if not root:
            return True

        # if the current node happens to be a right child,
        # it's supposed to be great than all previous max (rightmost position)
        if not (root.val > max_so_far):
            return False

        # if the current node happens to be a left child
        if not (root.val < min_so_far):
            return False

        cur_min, cur_max = min(min_so_far, root.val), max(max_so_far, root.val)

        return self.isValidBST(root.left,  cur_min, max_so_far) and \
            self.isValidBST(root.right, min_so_far, cur_max)
