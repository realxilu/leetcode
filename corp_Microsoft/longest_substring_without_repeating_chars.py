# [TWO-POINTER] i = start pointer, j = end pointer
class Solution:
    def lengthOfLongestSubstring(self, s):
        dic = {}
        i = j = 0
        _max = 0

        while j < len(s):
            # [TRICK] build the char dic counter
            dic[s[j]] = dic.get(s[j], 0) + 1

            # as long as the current char has appeared more than once (repeating chars)
            while dic.get(s[j]) > 1:
                # deduct the count since we will advance the start pointer 'i' in our next step
                dic[s[i]] -= 1
                # move the start pointer 'i' forward
                i += 1

            # NOTE the index to length conversion. index to length, always + 1, length to index always - 1
            _max = max(_max, j - i + 1)

            j += 1

        return _max

# [TRICK] dic[s[j]] = dic.get(s[j], 0) + 1 is the same as following
# if s[j] not in dic:
#   dic[s[j]] = 1
# else:
#   dic[s[j]] += 1

# [NOTE] you cannot advance 'i' first because the dictionary deduction still uses 'i'

