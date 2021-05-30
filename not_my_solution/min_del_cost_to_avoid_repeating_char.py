class Solution:
    def minCost(self, s, cost):
        res = max_cost = 0
        
        for i, _ in enumerate(s):
            # if the current element (i) and its next element aren't the same, reset max_cost
            if i > 0 and s[i] != s[i - 1]:
                max_cost = 0
            res += min(max_cost, cost[i])
            max_cost = max(max_cost, cost[i])

        return res

# whenever we have distinct neighboring elements, the max cost will be reset to zero
# for example, 1,2,3,4 for each step max cost will be reset
# 1,1,1,1,1,2,2,4,5: 1...1 the max cost wont' be reset till 1,2 happens  