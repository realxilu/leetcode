# [NOT_LEETCODE]Given an originally sorted array and find number of rotations that has een performed on the array
# num = [1 2 3 4 5] after 1 rotation [2 3 4 5 1]

def count_shift(nums):
    lo, hi, n = 0, len(nums) - 1, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        # need to understand this part
        prev = (mid - 1 + n) % n
        _next = (mid + 1) % n

        # cliff case: this step is not easy to think of in advanced
        if nums[prev] > nums[mid] and nums[_next] >= nums[mid]:
            return mid
        # look left
        elif nums[mid] < nums[lo]:
            hi = mid - 1
        # look right
        elif nums[mid] > nums[hi]:
            lo = mid + 1
        # no shit was made or the shift had occured n times
        else:
            return 0

# duplicates are then handled
count_shift([1, 1, 2, 1, 1])  # 3
count_shift([2, 1, 1, 1, 1])  # 1
