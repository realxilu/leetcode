#  KEY: math
#  sum = sum of the current array
#  m = number of steps to make the array all equal
#  n = length of the list
#  x = the unkown equal target number

# Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal,
# where a move is incrementing n - 1 elements by 1.

# eq 1: this is basically the statement of our problem
# m evolutions to (n - 1) elements, each evolution increments n - 1 elements by 1
# sum + m * 1 * (n - 1) = x * n

# eq 2: the min after m evolutions will become x
# min + m = x

# eq 1 + eq 2 then solve for m
# sum - min * n = m


class Solution:
    def min_moves(self, nums):
        sum_, min_ = sum(nums), min(nums)

        return sum_ - len(nums) * min_
