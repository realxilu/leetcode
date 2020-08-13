class Solution:
    def reverse_words(self, s):
        if not s:
            return s

        arr = s.split()
        arr.reverse()

        return ' '.join(arr)
