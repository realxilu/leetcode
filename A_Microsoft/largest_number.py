from functools import cmp_to_key


class Solution:
    def largest_number(self, nums):
        res = [str(x) for x in sorted(nums, key=cmp_to_key(self.comp), reverse=True)]

        if all(x == '0' for x in res):
            return '0'

        return ''.join(res)

    # KEY
    def comp(self, a, b):
        if str(a) + str(b) > str(b) + str(a):
            return 1
        else:
            return -1
