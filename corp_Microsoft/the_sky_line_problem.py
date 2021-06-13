from heapq import heappush, heappop
class Solution(object):
    def getSkyline(self, buildings):
        start_events = [(L, -H, R) for L, R, H in buildings]
        # note ending points' heights are all zero by definition
        end_events = [(R, 0, R) for _, R, _ in buildings]
        # [PYTHON] sort by tuple
        events = start_events + end_events
        events.sort()

        # NOTE both 'res' and 'heap' are dummy entries (much like sentinel nodes in linked list)
        # The reason for heap position of 0, hegiht with infinity x is that it will never be deqeued
        # the above manipulation is needed because heap[0] didn't exisit at the beginning and still need to be consumed in line 24
        # res: [start_coordinate, height]
        res = [(0, 0)]
        # heap:[height, ending position]
        heap = [(0, float('inf'))]

        # note cur_pos can either be a starting point or an ending point, cur_finish can only be an ending point
        for cur_pos, cur_height, cur_finish in events:
            # if the cur vertical line is touch or on the right side of heap max's ending, we remove the item from our heap
            while cur_pos >= (heap[0])[1]:  # heap[0][1]=max heap's ending position
                heappop(heap)
            # start events' heights aren't zero
            if cur_height:
                heappush(heap, (cur_height, cur_finish))
            # add current height to res only when it is different than the previous height
            # res[-1] denotes the last element in a list
            if res[-1][1] != -(heap[0])[0]:
                # NOTE the negative sign here, we are using an inverted min heap, thus the negative
                res += [(cur_pos, -(heap[0])[0])]

        return res[1:]

# [KEY][PRIORITY_QUEUE][HEAP]
# imagine of a vertical line scanning from left to right. we then use a heap to track the max height and ending position associtated with that max