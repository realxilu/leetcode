# i: start index, j: end index
# dp(i, j) represents whether s(i ... j) can form a palindromic substring
# dp(i, j) is true when s(i) equals to s(j) AND s(i + 1 ... j - 1)/enclosd string is palindromic.
# Time complexity O(n ^ 2).
class Solution:
    def longestPalindrome(self, s):
        res = ''
        dp = [[False for _ in s] for _ in s]

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i + 1 <= 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j + 1]

        return res

# [KEY][DP]
# j must be greater than or equal i at all times.
# Why? i is the start index of the substring, j is the end index of the substring.
# It makes no sense for i to be greater than j. Visualization helps me, so if you visualize the dp 2d array,
# think of a diagonal that cuts from top left to bottom right. 
# We are only filling the top right half of dp.
# Why are we counting down for i, but counting up for j? 
# Each sub-problem dp[i][j] depends on 
# dp[i+1][j-1](dp[i+1][j-1] must be true and s.charAt(i) must equal s.charAt(j) for dp[i][j] to be true).
