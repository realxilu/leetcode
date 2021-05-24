class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)

        for i in range(len(s)):
            if s[i] == '?':
                for c in 'abc':
                    # first letter then replace '?', last letter then replace '?'
                    # previous isn't the letter it is currently looking at then replace
                    # next isn't the letter it is currently looking at then replace
                    if (i == 0 or s[i - 1] != c) and (i == len(s) - 1 or s[i + 1] != c):
                        s[i] = c
                        break

        return ''.join(s)

# [KEY][OBSERVATION] 
# You don't need 26 letters in the alphabet, 'abc' is sufficent to generate non-consecutive number for any continuous '??????'
