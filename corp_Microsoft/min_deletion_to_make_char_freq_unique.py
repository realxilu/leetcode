import collections

class Solution:
    def minDeletions(self, s: str) -> int:
        dic, res, used = collections.Counter(s), 0, set()
        
        for freq in dic.values():
            while freq > 0 and freq in used:
                # make a deletion because we see this freq in 'used' set
                freq -= 1
                # record the deltion we just made so we can return it
                res += 1
            used.add(freq)
        
        return res

# collections.Counter(s) is the fastest way to create a freq table
