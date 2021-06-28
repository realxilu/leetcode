from collections import deque

def bfs_demo(node):
    q = deque([node])
    visited = set()

    while q:
        # print(q.val)
        visited.add(q)

        for nb in q.neigbhors:
            if nb not in visited:
                q.append(nb)

    
