# [TWO-POINTER]
def two_sum_closest(nums, target):
    nums.sort()

    left, right, min_ = 0, len(nums) - 1, float('inf')

    while left < right:
        diff = abs(target - nums[left] - nums[right])
        min_ = min(min_, diff)

        if nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1

    return min_
