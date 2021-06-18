class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic, rev_dic = {}, {}
        l1, l2 = list(pattern), s.split()
        if len(l1) != len(l2):
            return False

        for pat, word in zip(l1, l2):
            if pat not in dic:
                dic[pat] = word
            elif dic[pat] != word:
                return False

            if word not in rev_dic:
                rev_dic[word] = pat
            elif rev_dic[word] != pat:
                return False

        return True
