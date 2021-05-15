# [PRIROITY_QUEUE]
import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])

        # NOTE heap stores the end time of intervals
        heap = []
        for x in intervals:
            if heap and x[0] >= heap[0]:
                # means two intervals can use the same room
                heapq.heapreplace(heap, x[1])
            else:
                # a new room is allocated
                heapq.heappush(heap, x[1])

        return len(heap)

# x[0] = start of the interval
# x[1] = end of the interval