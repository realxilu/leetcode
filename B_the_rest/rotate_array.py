class Solution:
    def rotate(self, nums, k):
        len_ = len(nums)
        k = k % len_

        self._swap(nums, 0, len_ - 1)
        self._swap(nums, 0, k - 1)
        self._swap(nums, k, len_ - 1)

    def _swap(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
