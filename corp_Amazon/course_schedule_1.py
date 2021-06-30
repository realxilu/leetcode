class Solution:
    def canFinish(self, num_courses, prerequisites):
        # ajacency-list based graph
        graph = [[] for _ in range(num_courses)]
        # visited status table: status NEW | VISITED | DONE
        visited = ['NEW' for _ in range(num_courses)]

        # build graph
        # For example, the pair[5, 8], indicates that to take course 5 you have to first take course 8. 8=>5
        # NOTE graph[x].append(y) is semantically incorrect but it will NOT matter in this case
        for x, y in prerequisites:
            graph[y].append(x)

        # run dfs on each node
        for x in range(num_courses):
            # if run into a visited node aka detected a cycle return false
            if self.dfs(graph, visited, x) == False:
                return False

        return True

    # True means no cycle has been detected
    def dfs(self, graph, visited, i):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == 'VISITED':
            return False

        # all nodes are visited
        if visited[i] == 'DONE':
            return True

        # mark the current node as being visited
        visited[i] = 'VISITED'

        # visit all the neighbors
        for x in graph[i]:
            if self.dfs(graph, visited, x) == False:
                return False

        # after all visits, mark the node as done
        visited[i] = 'DONE'

        return True

# [KEY] dfs is the key to solving this puzzle