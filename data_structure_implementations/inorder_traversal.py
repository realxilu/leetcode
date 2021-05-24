def inorder(root):
    cur, stack = root, []

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        node = stack.pop()
        print(node.val)
        cur = node.right

# [KEY] stack memorizes the path leading up to the current node


