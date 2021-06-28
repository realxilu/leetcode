class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp, dp[0] = [False] * (len(s) + 1), True

        for i in range(1, len(s) + 1):
            for j in range(i):
                # if the previous words exist and substring bounded by j,i is in
                # the dictionary, then add ith position into the dictionary,break out and 
                # consider next i position
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]

# [KEY][DP] use dp to memorize the computed position to avoid the same calculation
