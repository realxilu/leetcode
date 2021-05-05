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

# method 2: Using Cyclic Replacements
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1

# method 3: brute force - swap out the array one by one
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


# method 4: copy using an extra array O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        arr = [0] * n

        for i in range(n):
            arr[(i + k) % n] = nums[i]

        # nums = arr won't work
        nums[:] = arr
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
