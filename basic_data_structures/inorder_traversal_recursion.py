def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.val)
    inorder(root.right)
