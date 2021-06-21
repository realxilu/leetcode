class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # visited[i]
        visited = [False] * len(isConnected)

        count = 0
        # visit each node
        for i in range(len(isConnected)):
            # if the current node is not visited
            if not visited[i]:
                count += 1
                self.dfs(isConnected, visited, i)

        return count

    # graph[i][j] has equal value of graph[j][i] which means two nodes are connected
    def dfs(self, graph, visited, i):
        for j in range(len(graph)):
            # if node i and j are connected and node j isn't visited
            if graph[i][j] == 1 and not visited[j]:
                visited[j] = True
                self.dfs(graph, visited, j)

# [DFS]
# TODO union-find
