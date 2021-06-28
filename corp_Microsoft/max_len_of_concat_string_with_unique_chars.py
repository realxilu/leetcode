class Solution:
    def maxLength(self, A):
        dp = [set()]
        for a in A:
            # if the current substring has dupes, we don't even bother considering it
            if len(set(a)) < len(a):
                continue
            # o.w. we turn it into set
            a = set(a)
            # note since dp will be operated on here, for the current loop we slice (make a copy of the original) using dp[:]
            # so we 'locked' the current dp
            for c in dp[:]:
                # if the current two have intersections, we skip
                if a & c:
                    continue
                # o.w. we add the union of set memeber 'a' and 'c'
                dp.append(a | c)

        return max(len(a) for a in dp)

# [KEY] set operations can be really really convenient sometimes
