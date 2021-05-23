class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
       
        stack = [-1] # NOTE this is NOT stack[-1]
        res = 0

        for i in range(len(height)):
            # as long as previous stacked heights are higher than the current height[i]
            while height[stack[-1]] > height[i]:
                h = height[stack.pop()]
                # NOTE this stack[-1] isn't the same as the previous stack[-1]
                width = i - stack[-1] - 1
                res = max(res, h * width)
            stack.append(i)

        return res

# [KEY] if previous heights are taller than the current height, keep popping them out of the stack
# previous heights don't have to be strictly descending as long as they are shorter than the current height
# the stack holds previously traversed indices


#
# x
# x x 
# x x x 
# x x x x
# x x x x
#       ^
#       |
#       i 
# case I: strictly descending

#     x
# x   x
# x x x
# x x x x
# x x x x
#       ^
#       |
#       i
# case II: not strictly descending, but all previous items are still smaller

#     x
#     x
#   x x
#   x x x
# x x x x
# ^     ^
# |     |
# stop  i
# the basic idea is to back scan from the current position 'i' to all previous bars as long as they are greater than it.
# [HINT] draw rectangles from the current position to previous position until hit the one that is smaller
# after done, move i to the left and do the above again
# after done, move i to the left and do the above again
# ...
# till hit stop

# [KEY] we can only use the shortest height to calculate the area

# [PYTHON] stack[-1] reveals the last element of the stack. This is the same as stack.peek() in Java

# [SIMILAR] to corp_Amazon\next_greater_element_1.py [STACK]

# [SIMILAR] [ALTERNATIVE] corp_Amazon\trap_rain_water.py
