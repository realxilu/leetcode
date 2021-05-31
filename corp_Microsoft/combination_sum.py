class Solution:
    # standard backtracking
    def combinationSum(self, candidates, target):
        res = []  # needs to be referenced to be returned
        self.backtrack(candidates, target, 0, [], res)

        return res

    # [KEY] need a tree diagram, things would be much easier
    # [KEY] there is a template for backtrack type of problems
    def backtrack(self, nums, target, index, path, res):
        if target < 0:
            return  # just backtrack here

        if target == 0:
            res.append(path)
            return  # add to res set then backtrack

        for i in range(index, len(nums)):
            self.backtrack(nums, target - nums[i], i, path + [nums[i]], res)

# [KEY] 'backtrack' and 'dfs' are standard names for naming recursive backtrack functions.
# This type of problems can be easily seen as a backtrack problem with diagrams. 
# Say the target is 7 and it is the root and then it has different combos as branches and leaves.
