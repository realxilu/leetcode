class Solution:
    def threeSumClosest(self, num, target):
        num.sort()
        _min = float('inf')

        for i in range(len(num) - 2):
            j, k = i + 1, len(num) - 1
            while j < k:
                _sum = num[i] + num[j] + num[k]
                if _sum == target:
                    return _sum

                if abs(_sum - target) < abs(_min - target):
                    _min = _sum

                if _sum < target:
                    j += 1
                elif _sum > target:
                    k -= 1

        return _min
