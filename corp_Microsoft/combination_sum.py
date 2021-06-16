class Solution:
    # standard backtracking
    def combinationSum(self, candidates, target):
        res = [] # pass by reference
        self.backtrack(candidates, target, 0, [], res)

        return res

    # [KEY] easier to visualize the problem by diagraming a tree, then it addresses the question why use backtrack
    # [KEY] utilize the template for backtracking problems
    def backtrack(self, nums, target, index, tmp_list, res):
        # exit condition I -- invalid:
        if target < 0:
            return  # just backtrack here

        # exit condition II -- harvest result:
        if target == 0:
            res.append(tmp_list)
            return  # add to res set then backtrack

        # [PYTHON] 'i' is moving in range(start, stop)
        for i in range(index, len(nums)):
            self.backtrack(nums, target - nums[i], i, tmp_list + [nums[i]], res)

# [KEY] 'backtrack' and 'dfs' are standard names for naming recursive backtrack functions.
# This type of problems can be easily seen as a backtrack problem with diagrams. 
# Say the target is 7 and it is the root and then it has different combos as branches and leaves.
