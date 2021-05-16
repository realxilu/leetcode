# [HEAPQ]
import heapq

class Solution:
    # cur_interval[0] = start of the interval
    # cur_interval[1] = end of the interval
    def minMeetingRooms(self, intervals):
        # sort intervals based on the starting time
        intervals.sort(key = lambda x: x[0])

        # NOTE 'rooms' only stores the *end* time of rooms
        rooms = []
        for cur_interval in intervals:
            # if the current interval's start is greater than or equal to the minimal end
            # roosm[0] is to 'peek' the min heap of the end time of the meeting rooms,
            # rooms[0]: the end time for soonest-ending meeting room
            if rooms and rooms[0] <= cur_interval[0]:
                # then we can pop out the earlier tenants of the meeting room
                # and push in the current tenants with its updated end time from the current interval
                # replace is a combined solution to pop out and push in
                heapq.heapreplace(rooms, cur_interval[1])
            else:
                # allocate a new room, NOTE end time of the current meeting
                heapq.heappush(rooms, cur_interval[1])

        return len(rooms)

# [KEY] learn to use priority queue
# heaprepalce = heap pop + heap push but more elegant

