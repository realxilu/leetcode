from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # max heap (invert min-heap) -> negative numbers
        self.large = []  # min heap -> positive numbers

    def addNum(self, num):
        if len(self.small) == len(self.large):
            # to heappushpop into small, we need negative numbers and before putting them into large we need reverse of that
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            # use negative numbers to mimic max heap and then flip the sign when poping
            # num is positive thus we need the heappushpop to be negative
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

# First of all what is a data stream. A data stream is data flow that pushes data to the user one at a time.
# [2, 4, 2, 1, 5, 3, 5] is a data stream that presents the data in an unorderly fashion
