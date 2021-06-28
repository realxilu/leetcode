class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {c: i for i, c in enumerate(order)}
        # words = [[4,2,1], [9,2,3,4,0,3], [8,2,1]]
        words = [[dic[c] for c in w] for w in words]

        # [TRICK] use zip to compare the first word and second word
        for w1, w2 in zip(words, words[1:]):
            if self.is_bigger(w1, w2):
                return False

        return True

    def is_bigger(self, s1, s2):
        m, n, i = len(s1), len(s2), 0
        while i < min(m, n):
            if s1[i] == s2[i]:
                i += 1
                continue
            return True if s1[i] > s2[i] else False

        return m > n

# [KEY] map 'world' => [4,3,2,1,8] using alien alphabet/order 'lrowabcdvnew'