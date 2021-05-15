class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts, ends = [], []

        for x in intervals:
            starts.append(x[0])
            ends.append(x[1])

        starts.sort()
        ends.sort()

        rooms, j = 0, 0
        for i in range(len(intervals)):
            if starts[i] < ends[j]:
                rooms += 1
            else:
                j += 1

        return rooms


