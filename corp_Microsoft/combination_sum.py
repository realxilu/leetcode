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
class Solution2:
    # faster
    def combination_sum(self, candidates, target):
        # note the dfs 'target' here is different than the target in combination_sum
        def dfs(target, arr):
            if target == 0:
                res.append(arr)
                return

            for x in candidates:
                if x > target:
                    break

                if arr and x < arr[-1]:  # '-1' means last element in the array
                    continue
                else:
                    dfs(target - x, arr + [x])
        # --------------------------------------

        res = []
        candidates = sorted(candidates)
        dfs(target, [])

        return res


class Solution3:
    def combination_sum(self, candidates, target):
        res = []
        self.dfs(target, [], sorted(candidates), res)

        return res

    def dfs(self, target, arr, candidates, res):
        if target == 0:
            res.append(arr)
            return

        for x in candidates:
            if x > target:
                break

            if arr and x < arr[-1]:
                continue
            else:
                self.dfs(target - x, arr + [x], candidates, res)
