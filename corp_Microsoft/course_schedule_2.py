# [TOPOSORT]
# TODO need to understand and write DFS + stack approach as well
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        # ajacency list
        graph = [[] for _ in range(numCourses)]
        # in-degree container
        in_degree = [set() for _ in range(numCourses)]

        # build graph and in-degree container
        for x, y in prerequisites:
            graph[y].append(x)
            in_degree[x].add(y)

        # If the current node doesn't have any in_degree, then it is a source. They don't depend on anyone now. Add them to the srcs list.
        res, srcs = [], [s for s in range(numCourses) if len(in_degree[s]) == 0]
        while srcs:  # srcs contains courses without prerequisites
            new_srcs = []
            for src in srcs:
                res.append(src)
                # visit all the neighbors of the sources, since we removed the current source, we deduct the in_degree of the neightbors
                for nbr in graph[src]:
                    in_degree[nbr].remove(src)
                    # if the in_degree of the current node becoms zero, add it to the new srcs
                    if len(in_degree[nbr]) == 0:
                        new_srcs.append(nbr)
            srcs = new_srcs  # new sources contains new courses with crossed-out prerequisites

        return res if len(res) == numCourses else []

# For example, the pair [x, y], indicates that to take course x you have to first take course y.
# That means y -> x. Be careful about ordering when building the ajacency list
# Note that the in-degree container is just the reverse, because we are counting incoming arrows to a node.

# srcs -> sources
# nbr  -> neighbor
