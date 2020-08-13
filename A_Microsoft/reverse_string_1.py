class Solution:
    def reverse_string(self, s):
        def reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        reverse(s, 0, len(s) - 1)
