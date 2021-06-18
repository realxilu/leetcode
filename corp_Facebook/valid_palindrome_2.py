class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
            else:
                return self.is_palindrome(s, l, r - 1) or self.is_palindrome(s, l + 1, r)

        return True

    def is_palindrome(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i, j = i + 1, j - 1
            else:
                return False

        return True
