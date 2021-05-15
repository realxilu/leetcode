class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_arr, right_arr = n * [0], n * [0]
        max_left, max_right = 0, 0

        for i in range(n):
            max_left = max(max_left, height[i])
            left_arr[i] = max_left

        for i in reversed(range(n)):
            max_right = max(max_right, height[i])
            right_arr[i] = max_right

        res = 0
        for i in range(n):
            water = min(left_arr[i], right_arr[i]) - height[i]

            if water > 0:
                res += water

        return res

# [KEY] maintain two arrays to track left max and right max
# left_arr[i] tracks the max water level seen so far from the left
# right_arr[i] tracks the max water level seen so far from the right
