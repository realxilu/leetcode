class Solution:
    def threeSumClosest(self, num, target):
        num.sort()
        _min = float('inf')

        for i in range(len(num) - 2):
            j, k = i + 1, len(num) - 1
            while j < k:
                cur_sum = num[i] + num[j] + num[k]
                if cur_sum == target:
                    return cur_sum

                if abs(cur_sum - target) < abs(_min - target):
                    _min = cur_sum

                if cur_sum < target:
                    j += 1
                elif cur_sum > target:
                    k -= 1

        return _min
