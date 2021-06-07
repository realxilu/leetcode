class Solution:
    def isValidBST(self, root):
        if not root:
            return True
        if not root.left and not root.right:
            return True

        return self.isValidBST(root.left) and  \
               self.isValidBST(root.right) and \
               self.get_max(root.left) < root.val < self.get_min(root.right)

    def get_min(self, node):
        if not node:
            return float('inf') # min is initialized to +infinity in case of a null node
        while node.left:
            node = node.left

        return node.val

    def get_max(self, node):
        if not node:
            return float('-inf') # max is initialzied to -infinity in case of a null node
        while node.right:
            node = node.right

        return node.val
    
    ## METHOD2: running min and max
    def isValidBST2(self, root, min_so_far=float('inf'), max_so_far=float('-inf')):
        if not root:
            return True

        # if the current node happens to be a right child
        # it's supposed to be great than all previous max (rightmost position)
        if not (root.val > max_so_far):
            return False

        # if the current node happens to be a left child
        if not (root.val < min_so_far):
            return False

        cur_min, cur_max = min(min_so_far, root.val), max(max_so_far, root.val)

        return self.isValidBST2(root.left,  cur_min, max_so_far) and \
               self.isValidBST2(root.right, min_so_far, cur_max)
