class Solution:
    def __init__(self):
        self.res = []
    
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return self.res
        
        self.res.append(root.val)
        
        self.add_left_boundary(root.left)
        self.add_leaves(root.left)
        self.add_leaves(root.right)
        self.add_right_boundary(root.right)
        
        return self.res
        
    def add_left_boundary(self, cur):
        if not cur or (not cur.left and not cur.right):
            return
        
        self.res.append(cur.val)
        
        if not cur.left:
            self.add_left_boundary(cur.right)
        else:
            self.add_left_boundary(cur.left)
        
    def add_right_boundary(self, cur):
        if not cur or (not cur.left and not cur.right):
            return
    
        if not cur.right:
            self.add_right_boundary(cur.left)
        else:
            self.add_right_boundary(cur.right)
            
        self.res.append(cur.val)
        
    def add_leaves(self, cur):
        if not cur:
            return
        
        if not cur.left and not cur.right:
            self.res.append(cur.val)
            return
        
        self.add_leaves(cur.left)
        self.add_leaves(cur.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
