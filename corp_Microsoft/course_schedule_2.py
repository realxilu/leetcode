# [TOPOSORT]
# TODO need to understand and write DFS + stack approach as well
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        # ajacency list
        graph = [[] for _ in range(numCourses)]
        # in_degree container
        in_degree = [set() for _ in range(numCourses)]

        # build graph and in-degree container
        for x, y in prerequisites:
            graph[y].append(x)
            in_degree[x].add(y)

        # If the current node doesn't have any in_degree, then it is a sources. They don't depend on anyone now. Add them to the sources list.
        res, sources = [], [s for s in range(numCourses) if len(in_degree[s]) == 0]
        while sources:  # sources contains courses without prerequisites
            new_sources = []
            for src in sources:
                res.append(src)
                # visit all the neighbors of the sources, since we removed the sources, we deduct the in_degree of the neightbors
                for nbr in graph[src]:
                    in_degree[nbr].remove(src)
                    # if the in_degree of the current node becoms zero, add it to the new sources
                    if len(in_degree[nbr]) == 0:
                        new_sources.append(nbr)
            sources = new_sources  # new_sources contains new courses with no prerequisites

        return res if len(res) == numCourses else []


# For example, the pair [x, y], indicates that to take course x you have to first take course y.
# That means y -> x. Be careful about ordering when building the ajacency list
# Note that the in_degree container is just the reverse since we care about incoming arrows
