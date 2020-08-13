class Solution:
    def reverse_words(self, s):
        res = []
        for word in s.split():
            res.append(word[::-1])

        return ' '.join(res)
