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


# method 2: brute force - swap out the array one by one
# one swap: [1, 2, 3, 4, 5] -> [5, 1, 2, 3, 4]
    def rotate(self, nums, k):
        k %= len(nums)

        # swap it for k times to achieve k rotations
        for _ in range(k):
            # record the last number
            prev = nums[-1]
            for i in range(len(nums)):
                nums[i], prev = prev, nums[i]

# explanation: first record the last element and then swap out 2nd elements to the last using prev