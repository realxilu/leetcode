import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []

        for (x, y) in points:
            dist = - (x * x + y * y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [(x, y) for (dist, x, y) in heap]

# [KEY]
# why do we have a negative sign in the Euclidean distance?
# Because we are faking the max heap here

# why do we want to use max-heap here?
# because we want to keep the smallest values possible

# Runtime:
# Inserting an item to a heap of size k take O(logK) time.
# And we do this for each item points.
# So runtime is O(N * logK) where N is the length of points.

# Space: O(K) for our heap.
