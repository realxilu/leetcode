class Solution:
    def canFinish(self, num_courses, prerequisites):
        # list comprehension
        graph = [[] for x in range(num_courses)]
        visited = [0 for x in range(num_courses)]

        # create an ajacency list graph
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)

        # run dfs starting from each node
        for x in range(num_courses):
            if not self.dfs(graph, visited, x):
                return False

        return True

    # True -> no cycle; False -> cycle detected
    def dfs(self, graph, visited, i):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == 'visited':
            return False

        # all nodes are visited
        if visited[i] == 'done':
            return True

        # mark the current node as being visited
        visited[i] = 'visited'

        # visit all the neighbors
        for x in graph[i]:
            if self.dfs(graph, visited, x) == False:
                return False

        # after all visit, finally mark it as done
        visited[i] = 'done'

        return True




