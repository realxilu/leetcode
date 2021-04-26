# [TWO-POINTER]
def two_sum_closest(nums, target):
    # [KEY]
    nums.sort()

    i, j = 0, len(nums) - 1
    _min = float('inf')

    while i < j:
        diff = abs(target - nums[i] - nums[j])
        _min = min(_min, diff)

        # [TIP] 'i' can only move to the right; j the left
        if nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1

    return _min
