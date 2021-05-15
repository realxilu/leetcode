# [PRIROITY_QUEUE]
import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        # sort intervals based on the starting time
        intervals.sort(key=lambda x: x[0])

        # NOTE heap only stores the end time of intervals
        heap = []
        for x in intervals:
            # if the current interval's start is greater than or equal to the minimal end
            # NOTE heap[0] is the 'peek' of the min heap of ends (thus giving us the min value), it is NOT the start of the heap
            if heap and x[0] >= heap[0]:
                # then we can pop out the earlier tenants of the meeting room and push in the current tenants
                # replace is a combined solution to pop out and push in
                heapq.heapreplace(heap, x[1])
            else:
                # a new room is allocated
                heapq.heappush(heap, x[1])

        return len(heap)

# x[0] = start of the interval
# x[1] = end of the interval