class Solution:
    def permute(self, nums):
        res = []

        # base case
        if len(nums) == 1:
            res.append(nums)
            return res

        for i, _ in enumerate(nums):
            # swap the 1st element with the ith element
            nums[i], nums[0] = nums[0], nums[i]
            # calculate the perm formed by the rest element
            rest_perms = self.permute(nums[1:])
            # add each perm with the first element
            for perm in rest_perms:
                res.append([nums[0]] + perm)

        return res
