class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        _max = 0

        for i in range(len(height)):
            while height[stack[-1]] > height[i]:
                h = height[stack.pop()]
                width = i - stack[-1] - 1
                _max = max(_max, h * width)
            stack.append(i)

        return _max

# [KEY] if previous heights are taller than the current height, keep popping them out of the stack
# the previous heights don't have to be strictly descending as long as they are shorter than the current height
# the stack records previously traversed indices 

# [KEY] we can only use the shortest height to calculate the area

# [SIMILAR] to next greater element
