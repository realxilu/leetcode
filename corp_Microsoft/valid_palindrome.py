# [TWO-POINTER]
class Solution:
    def isPalindrome(self, s):
        i, j = 0, len(s)-1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True

# learning points:
# - isalnum: is alphanumeric
# - lower: lower just one 'active' char instead of whole string