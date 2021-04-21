class Solution:
    def canFinish(self, num_courses, prerequisites):
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
        if visited[i] == 'visited':
            return False

        # If 'done' flag is set, that means all visits had been completed
        if visited[i] == 'done':
            return True

        # mark the current node as being visited
        visited[i] = 'visited'

        # visit all the neighbors
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False

        # after all visit, finally mark it as done
        visited[i] = 'done'

        return True




