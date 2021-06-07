class Solution:
    def isValidBST(self, root, prev_min=float('inf'), prev_max=float('-inf')):
        if not root:
            return True

        if root.val <= prev_max or root.val >= prev_min:
            return False

        cur_min = min(prev_min, root.val)
        cur_max = max(prev_max, root.val)

        return self.isValidBST(root.left,  cur_min, prev_max) and \
               self.isValidBST(root.right, prev_min, cur_max)
