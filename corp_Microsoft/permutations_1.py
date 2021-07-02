class Solution:
    def permute(self, nums):
        res = []

        if len(nums) == 1:
            res.append(nums)
            return res

        for i in range(len(nums)):
            # swap the 1st element with the ith element
            nums[i], nums[0] = nums[0], nums[i]
            # calculate the perm formed by the rest element
            rest_perms = self.permute(nums[1:])
            # add each permutation with the first element
            for perm in rest_perms:
                # NOTE '+' sign for array concatenation example: [1] + [4, 9] = [1, 4, 9]
                res.append([nums[0]] + perm)

        return res

# This is the preferred solution
# [KEY] NOTE the return value here. The return value should be permutations of any sized (could be reduced) arrays
# [EXAMPLE] take out the first number, do perm on the rest
# [A, B, C] => [A] + perm([B, C]) | [B] + perm([A, C]) | [C] + perm([A, B])
# [B, C] => [B] + perm([C]) | [C] + perm([B])
# [A, C] => [A] + perm([C]) | [C] + perm([A])
# [A, B] => [A] + perm([B]) | [B] + perm([A])
