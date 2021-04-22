class Solution:
    def compare_version(self, v1, v2):
        l1, l2 = v1.split('.'), v2.split('.')

        l1 = list(map(lambda x: int(x), l1))
        l2 = list(map(lambda x: int(x), l2))

        l1_len, l2_len = len(l1), len(l2)
        min_len, max_len = min(l1_len, l2_len), max(l1_len, l2_len)

        i = 0
        while i < min_len:
            if l1[i] < l2[i]:
                return -1
            if l1[i] > l2[i]:
                return 1
            i += 1

        while i < max_len:
            if i >= len(l1) and l2[i] > 0:
                return -1
            if i >= len(l2) and l1[i] > 0:
                return 1
            i += 1

        return 0
