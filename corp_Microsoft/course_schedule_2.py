# [TOPOSORT]
# TODO need to understand and write DFS + stack approach as well
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        # ajacency list
        graph = [[] for _ in range(numCourses)]
        # indegree container
        indegree = [set() for _ in range(numCourses)]

        # build graph and in-degree container
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x].add(y)

        # If the current node doesn't have any indegree, then it is a source. They don't depend on anyone now. Add them to the source list.
        res, source = [], [s for s in range(numCourses) if len(indegree[s]) == 0]
        while source:  # source contains courses without prerequisites
            new_source = []
            for s in source:
                res.append(s)
                # visit all the neighbors of the source, since we removed the source, we deduct the indegree of the neightbors
                for i in graph[s]:
                    indegree[i].remove(s)
                    # if the indegree of the current node becoms zero, add it to the new source
                    if len(indegree[i]) == 0:
                        new_source.append(i)
            source = new_source  # new_source contains new courses with no prerequisites

        return res if len(res) == numCourses else []


# For example, the pair [x, y], indicates that to take course x you have to first take course y.
# That means y -> x. Be careful about ordering when building the ajacency list
# Note that the indegree container is just the reverse since we care about incoming arrows
