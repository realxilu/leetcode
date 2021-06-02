class Solution:
    # O(nlogn)
    def firstMissingPositive(self, A):
        s = set()
        for x in A:
            if x > 0:
                s.add(x)

        i = 0
        for i, x in enumerate(sorted(list(s))):
            if x - i > 1:
                return i + 1

        return x + 1 if x > 0 else 1

# [KEY] don't be lazy, diagram it out. sometimes it is hard to think inside your head without viz
# Once I wrote out the indices and numbers, the relationship between x and i became much claerer.

# TODO above is not the optimal solution


# class Solution {
#     public:
#     int firstMissingPositive(vector < int > & nums) {
#         int i = 0
#         int n = nums.size()
#         while (i < n)
#         {
#             if (nums[i] > 0 & & nums[i] <= n & & nums[nums[i] - 1] != nums[i])
#               swap(nums[i], nums[nums[i]-1])
#             else
#               i++
#         }
#         for (i=0#              i < n#              + +i)
    #         if (nums[i] != (i+1))
    #           return i+1
#         return n+1
#     }
# }
