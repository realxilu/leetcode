class Solution:
    def reverseWords(self, s):
        l = s.split()

        i, j = 0, len(l) - 1

        # [IN-PLACE] 
        while i < j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1

        return ' '.join(l).strip()
