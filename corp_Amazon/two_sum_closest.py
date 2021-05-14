def two_sum_closest(nums, target):
    # [KEY]
    nums.sort()

    i, j = 0, len(nums) - 1
    _min = float('inf')

    while i < j:
        diff = abs(nums[i] + nums[j] - target)
        _min = min(_min, diff)

        # [TIP] 'i' can only move to the right and 'j' only the left due to the ordering
        if nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1

    return _min

# [TWO-POINTER]
# [KEY] the array needs to be sorted for two pointer to work