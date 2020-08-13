from collections import deque


class Solution:
    def clone_graph(self, root):
        dic = {}

        # 1st BFS: create node-to-node mapping
        q = deque([root])
        while q:
            node = q.popleft()
            dic[node] = Node(node.val, [])

            for nb in node.neighbors:
                if nb not in dic:
                    q.append(nb)

        # 2nd BFS: associate nodes
        q = deque([root])
        s = set()
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
        self.neighbors = neighbors
