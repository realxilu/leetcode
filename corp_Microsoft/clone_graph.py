from collections import deque
class Solution:
    def cloneGraph(self, root):
        if not root:
            return None

        # 1st BFS: create node-to-node mapping
        dic, q = {}, deque([root])
        while q:
            node = q.popleft()
            dic[node] = Node(node.val, [])

            for nb in node.neighbors:
                if nb not in dic:
                    q.append(nb)

        # 2nd BFS: associate nodes
        q, s = deque([root]), set()
        while q:
            node = q.popleft()

            if node not in s:
                s.add(node)

                for nb in node.neighbors:
                    if nb not in s:
                        q.append(nb)
                    # associate nodes
                    dic[node].neighbors.append(dic[nb])

        return dic[root]


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors  # list

# [KEY] bfs traversal + hashmap
# 1st pass created mapped nodes
# 2nd pass establish relationships between the old and new
