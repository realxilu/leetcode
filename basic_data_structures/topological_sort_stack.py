from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topological_sort
    def topological_sort_util(self, v, visited, list_):
        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for x in self.graph[v]:
            if visited[x] == False:
                self.topological_sort_util(x, visited, list_)

        # Push current vertex to list_ which stores result
        list_.insert(0, v)

    # The function to do Topological Sort. It uses recursive
    # topological_sort_util()
    def topological_sort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        list_ = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for x in range(self.V):
            if visited[x] == False:
                self.topological_sort_util(x, visited, list_)

        # Print contents of the list_
        print(list_)


g = Graph(6)

g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

g.topological_sort()
