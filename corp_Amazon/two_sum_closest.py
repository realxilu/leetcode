def two_sum_closest(nums, target):
    # [KEY]
    nums.sort()
    i, j, _min = 0, len(nums) - 1, float('inf')

    while i < j:
        diff = abs(nums[i] + nums[j] - target)
        _min = min(_min, diff)

        # [TIP] 'i' only moves to the right and 'j' left
        if nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1

    return _min

# [KEY][TWO-POINTER] the array needs to be sorted for two pointer to work
