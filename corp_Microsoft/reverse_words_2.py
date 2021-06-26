class Solution:
    def reverseWords(self, s: List[str]) -> None:
        self.reverse(s, 0, len(s) - 1)

        start = 0
        for i, _ in enumerate(s):
            if s[i] == ' ':
                self.reverse(s, start, i - 1)
                start = i + 1

        self.reverse(s, start, len(s) - 1)

    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
