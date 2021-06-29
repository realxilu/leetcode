class Solution:
    def threeSumClosest(self, nums, target):
        # NOTE important to sort the array
        nums.sort()
        _min = float('inf')

        # be careful about edge indices
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum == target:
                    return cur_sum

                # compare the dist btw current optimal and historial optimal so far
                if abs(cur_sum - target) < abs(_min - target):
                    _min = cur_sum

                if cur_sum < target:
                    j += 1
                elif cur_sum > target:
                    k -= 1

        return _min

# [KEY][TWO-POINTER]