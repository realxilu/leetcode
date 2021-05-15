# [PRIROITY_QUEUE]
import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])

        # stores the end time of intervals
        heap = []
        for interval in intervals:
            if heap and interval[0] >= heap[0]:
                # means two intervals can use the same room
                heapq.heapreplace(heap, interval[1])
            else:
                # a new room is allocated
                heapq.heappush(heap, interval[1])

        return len(heap)

# interval[0] = start of the interval
# interval[1] = end of the interval