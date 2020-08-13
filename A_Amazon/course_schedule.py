class Solution:
    def can_finish(self, num_courses, prerequisites):
        # list comprehension
        graph = [[] for _ in range(num_courses)]
        visited = [0 for _ in range(num_courses)]

        # create graph - ajacency list
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)

        # run dfs starting from each node
        for i in range(num_courses):
            if not self.dfs(graph, visited, i):
                return False

        return True

    # True <==> No cycle
    def dfs(self, graph, visited, i):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False

        # if it is done visted, then do not visit again
        if visited[i] == 1:
            return True

        # mark as being visited
        visited[i] = -1

        # visit all the neighbors
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False

        # after visit all the neighbors, mark it as done visited
        visited[i] = 1

        return True
