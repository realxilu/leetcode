# [TWO-POINTER]
class Solution:
    def lengthOfLongestSubstring(self, s):
        dic = {}
        i = j = 0
        _max = 0

        while j < len(s):
            dic[s[j]] = dic.get(s[j], 0) + 1

            while dic[s[j]] > 1:
                dic[s[i]] -= 1
                i += 1

            _max = max(_max, j - i + 1)

            j += 1

        return _max
