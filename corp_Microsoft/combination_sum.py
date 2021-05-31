class Solution1:
    # standard backtracking
    def combination_sum(self, candidates, target):
        res = []  # needs to be referenced to be returned
        self.dfs(candidates, target, 0, [], res)

        return res

    # [KEY] need a tree diagram, things would be much easier
    # [KEY] there is a template for backtrack type of problems
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # just backtrack here

        if target == 0:
            res.append(path)
            return  # add to res set then backtrack

        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)

# [KEY] 'dfs' and 'backtrack' are common names for backtrack type of problems.
# It can be easily seen as a backtrack problem with diagrams. Say the target is 7 and it is the root and then it has different combos as branches and leaves.

# 'return' is synonymous as backtrack
